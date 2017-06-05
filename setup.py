#!/usr/bin/python3

""" Do setup for bindex package. """

import re
from distutils.core import setup
__version__ = re.search(r"__version__\s*=\s*'(.*)'",
                        open('src/bindex/__init__.py').read()).group(1)

# see http://docs.python.org/distutils/setupscript.html

setup(name='bindex',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      py_modules=[],
      packages=['src/bindex'],
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
