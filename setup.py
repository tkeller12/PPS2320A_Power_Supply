
import setuptools
from distutils.core import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("pps/version.py", "r") as f:
    # Define __version__
    exec(f.read())

setup(
    name="pps",
    packages=setuptools.find_packages(),
    version=__version__,
    license="MIT",
    description="Python Package for Controlling Circuit Specialists DC Power Supply PPS2320A",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Timothy Keller",
    url="",
    download_url="",
    project_urls={
    },
    keywords=["PPS2320A", "Power Supply", "Circuit Specialists"],
    python_requires=">=3.6",
    install_requires=[
        "pyserial",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)

