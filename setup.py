from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in travel_module/__init__.py
from travel_module import __version__ as version

setup(
	name="travel_module",
	version=version,
	description="Travel Module for Travel industry",
	author="SMB",
	author_email="usamanaveed9263@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
