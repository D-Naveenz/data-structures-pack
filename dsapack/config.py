import os


def get_version() -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open
    with open(os.path.join(here, "__init__.py")) as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                # __version__ = "0.1.0"
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        raise RuntimeError("Unable to find version string.")


__version__ = get_version()
__version_min__ = "0.12"


def validate_version(version: str) -> bool:
    _current = float(version)
    _min = float(__version_min__)

    if _current >= _min:
        return True
    else:
        return False
