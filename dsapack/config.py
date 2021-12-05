import os


def get_version() -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open
    with open(os.path.join(here, "__init__.py")) as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                # __version__ = "0.9"
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        raise RuntimeError("Unable to find version string.")


__version__ = get_version()
