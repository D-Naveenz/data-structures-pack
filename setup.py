import json

from setuptools import setup

with open("data_structures/config.json", "r") as info:
    config: dict = json.load(info)

try:
    import pypandoc

    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='data_structures',
    packages=['data_structures', 'data_structures.graph', 'data_structures.stack'],
    license='LICENSE.txt',
    **config["pkg_info"],
    long_description=long_description
)
