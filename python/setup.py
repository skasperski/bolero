from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

import bolero
import pkgconfig

# Run Cython to create cpp-sources from .pyx files
cythonize("bolero/wrapper/_wrapper.pyx")
cythonize("bolero/utils/_ranking_svm.pyx")

# Use PkgConfig to configure the extensions
conf = pkgconfig.parse("bl_loader bolero lib_manager")


ranking = Extension('bolero/utils/_ranking_svm', ['bolero/utils/_ranking_svm.c'])
wrapper = Extension('bolero/wrapper/_wrapper', ['bolero/wrapper/_wrapper.cpp'],
	include_dirs = conf["include_dirs"],
	library_dirs = conf["library_dirs"],
	libraries = conf["libraries"]
)

# Create the Python package with setuptools
setup(
	name="bolero",
	maintainer="DFKI-RIC",
	maintainer_email="behavior-learning@dfki.de",
	description="Behavior Optimization and Learning for Robots",
	license="BSD 3-clause",
	version=bolero.__version__,
	url="http://robotik.dfki-bremen.de/en/research/softwaretools/bolero.html",
	download_url="https://github.com/rock-learning/bolero/archive/master.zip",
	scripts = ["bolero/scripts/bolero-run"],
	packages=find_packages(),
	ext_modules=[ranking, wrapper],
)

