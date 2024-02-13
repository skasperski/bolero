from setuptools import setup, find_packages, Extension

import bolero

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
	ext_modules=[Extension('bolero/utils/_ranking_svm', ['bolero/utils/_ranking_svm.c'])],
)

