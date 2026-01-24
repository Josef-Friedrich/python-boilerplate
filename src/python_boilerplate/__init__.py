from importlib import metadata

__version__: str = metadata.version("python_boilerplate")


def print_version() -> None:
    """Print the version of the package."""
    version = __version__
    print(version)
