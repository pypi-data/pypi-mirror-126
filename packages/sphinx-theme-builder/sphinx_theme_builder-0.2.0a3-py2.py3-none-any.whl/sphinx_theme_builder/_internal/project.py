"""Metadata and file system logic goes here."""

import ast
import configparser
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Literal, Mapping, NewType, Optional, Tuple

import tomli
from packaging.utils import canonicalize_name
from packaging.version import InvalidVersion, Version
from rich.text import Text

from .errors import DiagnosticError

Metadata = NewType("Metadata", Mapping[str, Any])


def read_toml_file(path: Path) -> "Mapping[str, Any]":
    with path.open("rb") as stream:
        return tomli.load(stream)


def get_version_using_ast(contents: bytes) -> Optional[str]:
    """Extract the version from the given file, using the Python AST."""
    tree = ast.parse(contents)

    # Only need to check the top-level nodes, and not recurse deeper.
    version: Optional[str] = None
    for child in tree.body:
        # Look for a simple string assignment to __version__
        if (
            isinstance(child, ast.Assign)
            and len(child.targets) == 1
            and isinstance(child.targets[0], ast.Name)
            and child.targets[0].id == "__version__"
            and isinstance(child.value, ast.Str)
        ):
            version = child.value.s
            break

    return version


class ImproperProjectMetadata(DiagnosticError):
    """For issues with pyproject.toml contents or other metadata."""


class InvalidProjectStructure(DiagnosticError):
    """For issues with the project structure."""


def _load_pyproject(pyproject: Path) -> Tuple[str, Metadata, Dict[str, Any]]:
    """Load from the pyproject.toml file, doing the minimal sanity checks."""
    try:
        pyproject_data = read_toml_file(pyproject)
    except FileNotFoundError as error:
        raise InvalidProjectStructure(
            message="Could not find a `pyproject.toml`.",
            context=f"Looked at {pyproject}",
            hint_stmt="Is this a valid Python package?",
            reference="pyproject-missing",
        ) from error
    except tomli.TOMLDecodeError as error:
        raise ImproperProjectMetadata(
            message="Could not parse `pyproject.toml`.",
            context=f"{error}\npath: {pyproject}",
            hint_stmt=None,
            reference="pyproject-could-not-parse",
        ) from error

    if (project := pyproject_data.get("project", None)) is None:
        raise ImproperProjectMetadata(
            message=Text("Could not find [project] table."),
            context=f"in file {pyproject}",
            hint_stmt=None,
            reference="pyproject-no-project-table",
        )

    if (kebab_name := project.get("name", None)) is None:
        raise ImproperProjectMetadata(
            message=Text("Could not find `name` in [project] table."),
            context=f"in file {pyproject}",
            hint_stmt=None,
            reference="pyproject-no-name-in-project-table",
        )

    if kebab_name != (canonical_name := canonicalize_name(kebab_name)):
        raise ImproperProjectMetadata(
            message=Text("Found non-canonical `name` declared in the [project] table."),
            context=(
                f"Got '{kebab_name}', expected '{canonical_name}'\n"
                f"in file {pyproject}"
            ),
            hint_stmt=None,
            reference="pyproject-non-canonical-name",
        )

    configuration: Dict[str, Any] = pyproject_data.get("tool", {}).get(
        "sphinx-theme-builder", {}
    )
    metadata: Metadata = pyproject_data.get("project", {})

    return kebab_name, metadata, configuration


def _determine_version(
    package_path: Path, kebab_name: str, metadata: Metadata
) -> Tuple[str, Literal["pyproject.toml", "__init__.py"]]:
    # Let's look for the version now!
    declared_in_python = None  # type: Optional[str]
    declared_in_pyproject = None  # type: Optional[str]

    # Load the version from pyproject.toml file, if provided.
    if "version" in metadata:
        declared_in_pyproject = metadata["version"]
        if not isinstance(declared_in_pyproject, str):
            raise ImproperProjectMetadata(
                message=Text(
                    "Expected 'version' in the [project] table to be a string."
                ),
                context=(
                    f"Got {declared_in_pyproject} which is {type(declared_in_pyproject)} instead."
                ),
                hint_stmt=None,
                reference="pyproject-invalid-version",
            )

    # Load the version from __init__ file, if provided.
    package_init_file = package_path / "__init__.py"
    if not package_init_file.exists():
        raise InvalidProjectStructure(
            message=f"{package_init_file} is missing.",
            context=(
                "It is required for this package to be a Sphinx theme.\n"
                f"The declared project name is {kebab_name}."
            ),
            hint_stmt=None,
            reference="project-init-missing",
        )

    try:
        declared_in_python = get_version_using_ast(package_init_file.read_bytes())
    except SyntaxError as error:
        raise InvalidProjectStructure(
            message="Could not parse `__init__.py` file",
            context=f"In file {package_init_file}\n{error!r}",
            hint_stmt=None,
            reference="project-init-invalid-syntax",
        ) from error

    if declared_in_pyproject and declared_in_python:
        raise InvalidProjectStructure(
            message="Found version declaration in both `pyproject.toml` and `__init__.py`.",
            context=(
                "The package version MUST only be provided information in one location"
                f"\nFrom `pyproject.toml`, got {declared_in_pyproject}"
                f"\nFrom `__init__.py`, got {declared_in_python}"
            ),
            hint_stmt=Text(
                "It is a good idea to declare the version in Python alone.\n"
                "You can do this by removing `project.version` from `pyproject.toml` "
                'and including "version" in the `project.dynamic` list. Like so:\n\n'
                "[project]\n"
                'dynamic = ["version"]'
            ),
            reference="project-double-version-declaration",
        )
    elif declared_in_python:
        if "version" not in metadata.get("dynamic", []):
            raise ImproperProjectMetadata(
                message=(
                    "Found version in `__init__.py` but pyproject.toml does not "
                    'include "version" in `project.dynamic` list.'
                ),
                context=f"From `__init__.py`, got version {declared_in_python}",
                hint_stmt=Text(
                    'You solve this by including "version" in the `project.dynamic` '
                    "list. Like so:\n\n"
                    "[project]\n"
                    'dynamic = ["version"]'
                ),
                reference="project-missing-dynamic-version",
            )
        return (declared_in_python, "__init__.py")
    elif declared_in_pyproject:
        if "version" in metadata.get("dynamic", []):
            raise ImproperProjectMetadata(
                message=(
                    'Declared "version" as `dynamic`, while also using `version` key '
                    "in `pyproject.toml`."
                ),
                context=f"From `pyproject.toml`, got version {declared_in_pyproject}.",
                hint_stmt=(
                    "You can solve this by removing `version` from `project.dynamic`."
                ),
                reference="project-improper-dynamic-version",
            )
        return (declared_in_pyproject, "pyproject.toml")

    raise InvalidProjectStructure(
        message="No version declaration found for project.",
        context=f"Looked at {package_init_file} and corresponding `pyproject.toml`.",
        hint_stmt=(
            "Did you forget to declare the version? "
            "It's the 'project.version' key in `pyproject.toml` "
            "and the `__version__` attribute in `__init__.py`."
        ),
        reference="project-no-version-declaration",
    )


@dataclass(frozen=True)
class Project:
    """Represents a project to be built."""

    kebab_name: str
    # theme_name: str
    version: Version
    location: Path
    metadata: Metadata
    configuration: Dict[str, Any]

    @classmethod
    def from_cwd(cls) -> "Project":
        retval = cls.from_path(Path.cwd())
        retval.validate_file_structure_and_contents()
        return retval

    @classmethod
    def from_path(cls, path: Path) -> "Project":
        """Load a project from given Path."""
        pyproject = path / "pyproject.toml"
        kebab_name, metadata, configuration = _load_pyproject(pyproject)

        # IMPORTANT: Keep in sync with `python_package_path` below.
        package_path = path / "src" / kebab_name.replace("-", "_")
        version_s, version_comes_from = _determine_version(
            package_path, kebab_name, metadata
        )

        try:
            version = Version(version_s)
        except InvalidVersion as error:
            raise ImproperProjectMetadata(
                message=f"Got an invalid version: {version_s}",
                context=f"This came from `{version_comes_from}`",
                hint_stmt=None,
                reference="project-invalid-version",
            ) from error

        return Project(
            kebab_name=kebab_name,
            version=version,
            location=path,
            metadata=metadata,
            configuration=configuration,
        )

    @property
    def snake_name(self) -> str:
        return self.kebab_name.replace("-", "_")

    @property
    def source_path(self) -> Path:
        return self.location / "src"

    @property
    def python_package_path(self) -> Path:
        return self.source_path / self.snake_name

    @property
    def theme_path(self) -> Path:
        # TODO: Allow mismatch between theme name and PyPI name.
        return self.python_package_path / "theme" / self.kebab_name

    @property
    def theme_static_path(self) -> Path:
        return self.theme_path / "static"

    @property
    def assets_path(self) -> Path:
        return self.python_package_path / "assets"

    @property
    def theme_conf_path(self) -> Path:
        return self.theme_path / "theme.conf"

    @property
    def input_scripts_path(self) -> Path:
        return self.assets_path / "scripts"

    @property
    def output_script_path(self) -> Path:
        return self.theme_static_path / "scripts" / (self.kebab_name + ".js")

    @property
    def input_stylesheets_path(self) -> Path:
        return self.assets_path / "styles"

    @property
    def output_stylesheet_path(self) -> Path:
        return self.theme_static_path / "styles" / (self.kebab_name + ".css")

    @property
    def output_extension_stylesheet_path(self) -> Path:
        return self.theme_static_path / "styles" / (self.kebab_name + "-extensions.css")

    @property
    def compiled_assets(self) -> Tuple[str, ...]:
        """A sequence of compiled assets, as relative POSIX paths (to project root)."""
        files = tuple(
            map(
                (lambda path: path.relative_to(self.location).as_posix()),
                [
                    self.output_script_path,
                    self.output_stylesheet_path,
                    self.output_extension_stylesheet_path,
                ],
            )
        )
        # Tack on the .map files
        return files + tuple(map((lambda x: x + ".map"), files))

    def validate_file_structure_and_contents(self) -> None:
        """Validate the project's file structure and check that it matches the template.

        This is an important diagnostic step, to present useful and clear error messages
        to users who are transitioning from an existing theme to this one.
        """
        #
        # File presence
        #
        package_init_file = self.python_package_path / "__init__.py"
        assert (
            package_init_file.exists()
        ), "This should've been validated in `Project.from_path`"

        if not self.theme_conf_path.exists():
            raise InvalidProjectStructure(
                message=f"{self.theme_conf_path} does not exist.",
                context="It is required for this package to be a Sphinx theme.",
                hint_stmt=None,
                reference="missing-theme-conf",
            )

        if not self.input_scripts_path.exists():
            raise InvalidProjectStructure(
                message=f"{self.input_scripts_path} does not exist.",
                context="It is required for this package to be a Sphinx theme.",
                hint_stmt=None,
                reference="missing-javascript",
            )

        if not self.input_stylesheets_path.exists():
            raise InvalidProjectStructure(
                message=f"{self.input_stylesheets_path} does not exist.",
                context="It is required for this package to be a Sphinx theme.",
                hint_stmt=None,
                reference="missing-stylesheet",
            )

        #
        # File contents
        #
        expected_stylesheet = self.output_stylesheet_path.relative_to(
            self.theme_static_path
        ).as_posix()

        theme_conf_parser = configparser.ConfigParser()
        try:
            with self.theme_conf_path.open() as file:
                theme_conf_parser.read_file(file, source=file.name)
            specified_stylesheet = theme_conf_parser.get("theme", "stylesheet")
        except (OSError, configparser.Error) as error:
            raise InvalidProjectStructure(
                message=f"Could not open/parse {self.theme_conf_path}.",
                context=str(error),
                hint_stmt=None,
                reference="could-not-read-theme-conf",
            ) from error

        if specified_stylesheet != expected_stylesheet:
            raise InvalidProjectStructure(
                message=f"Incorrect stylesheet set in {self.theme_conf_path}.",
                context=f"Expected {expected_stylesheet}, got {specified_stylesheet}.",
                hint_stmt=None,
                reference="theme-conf-incorrect-stylesheet",
            )

        # TODO: Validate PEP 621 data.

    def get_metadata_file_contents(self) -> str:
        lines = [
            "Metadata-Version: 2.1",
            f"Name: {self.kebab_name}",
            f"Version: {self.version}",
        ]
        # TODO: Add metadata from PEP 621.
        return "\n".join(lines)

    def get_license_contents(self) -> str:
        # TODO: Add metadata from PEP 621.
        return ""

    def get_entry_points_contents(self) -> str:
        # TODO: Add metadata from PEP 621.
        return ""
