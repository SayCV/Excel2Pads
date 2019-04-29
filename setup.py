#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup
import json
import os

pkginfo_path = os.path.join(os.path.dirname(__file__),
                            '',
                            'pyExcel2Pads_info.json')
pkginfo = json.load(open(pkginfo_path))

setup(name=pkginfo['name'],
      version=pkginfo['version'],
      description=pkginfo['description'],
      author=pkginfo['main_author'],
      author_email=pkginfo['main_author_email'],
      url=pkginfo['url'],
      license=pkginfo['license'],
      packages=['src', ],
      package_data={'pyExcel2Pads': ['pyExcel2Pads_info.json']},
      scripts=['pyExcel2Pads.bat', 'pyExcel2Pads.py', 'pyExcel2Pads'],
      install_requires=[],
      requires=[],
      # include_dirs=[numpy.get_include()],
      setup_requires=[],
      tests_require=[],
      #long_description=open('README.md', 'r').read(),
      )
