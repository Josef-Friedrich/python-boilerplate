from importlib import metadata

__version__: str = metadata.version('python_project_boilerplate')


def print_version() -> None:
    version = __version__
    print(version)
