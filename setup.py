import os

# noinspection Mypy
from setuptools import setup

try:
    import pypandoc

    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name='dsapack',
    version=get_version("dsapack/config.py"),
    packages=['dsapack', 'dsapack.core'],
    project_urls={
        "Documentation": "https://pip.pypa.io",
        "Source": "https://github.com/D-Naveenz/data-structures-pack/",
        "Changelog": "https://github.com/D-Naveenz/data-structures-pack/blob/master/CHANGELOG.md",
    },
    license='AGPL-3.0',
    author='Naveen Dharmathunga',
    author_email='dnd.pro@outlook.com',
    description='Data structures package that commonly using in programming',
    long_description=long_description
)
