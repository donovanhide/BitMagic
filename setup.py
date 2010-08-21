import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages, Extension
import sys, os

version = '0.2.1'

bm_ext_extra = {}
try:
	import local_build
	for k in local_build.__dict__:
		if k.startswith("_") or k == "include_dirs":
			continue
		bm_ext_extra[k] = local_build.__dict__[k]
	if hasattr(local_build, "include_dirs"):
		include_dirs = local_build.include_dirs
	else:
		include_dirs =  []
except ImportError:
	include_dirs = []

workdir = os.getcwd()
srcdir = os.path.join(workdir, "src")
incdir = os.path.join(srcdir, "include")

bm_ext = Extension(
	name="bm_ext",
	sources=["src/bm.cpp"],
	include_dirs=[incdir] + include_dirs,
	libraries=["boost_python"],
	**bm_ext_extra
)

setup(name='bitmagic',
	version=version,
	description="Python wrapper for BitMagic",
	long_description="""\
Python wrapper for BitMagic C++ Library

BitMagic is available from http://bmagic.sourceforge.net/

These Python bindings contain software that is
Copyright(c) 2002-2009 Anatoliy Kuznetsov(anatoliy_kuznetsov at yahoo.com)

This software requires the Boost library from http://www.boost.org/
built with Python support.
""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='binary vector',
	author='William Waites',
	author_email='wwaites_at_gmail.com',
	url='http://pypi.python.org/pypi/bitmagic',
	license='BSD',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
	    # -*- Extra requirements: -*-
	],
	entry_points="""
	# -*- Entry points: -*-
	""",
	ext_modules=[bm_ext],

	)
