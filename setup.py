#!/usr/bin/python3

""" Do setup for bindex package. """

import re

# BEGIN NEW
from glob import glob
from os.path import basename, dirname, join, splitext
from setuptools import find_packages, setup
# END NEW

__version__ = re.search(r"__version__\s*=\s*'(.*)'",
                        open('src/bindex/__init__.py').read()).group(1)

# see
# setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords

with open('README.md', 'r') as file:
    long_desc = file.read()

setup(name='bindex',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',

      # BEGIN NEW
      long_description=long_desc,
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
      include_package_data=False,
      zip_safe=False,
      # END NEW

      # following could be in scripts/ subdir
      scripts=[],
      description="index content-keyed files",
      url='https://jddixon.github.io/bindex',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
