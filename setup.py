from setuptools import setup
from data_structures.cofig import *

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='data_structures',
    version=VERSION,
    packages=['data_structures', 'data_structures.graph', 'data_structures.stack'],
    url='https://github.com/D-Naveenz/data-structures-pack',
    license='LICENSE.md',
    author='Naveen Dharmathunga',
    author_email='dnd.pro@outlook.com',
    description='Data structures package that commonly using in programming',
    long_description=long_description
)
