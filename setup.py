"""
ChromeCloak - Modern anti-detection Chrome automation library
Inspired by and based on undetected-chromedriver
(https://github.com/ultrafunkamsterdam/undetected-chromedriver)

!!! LEGACY INSTALLATION METHOD !!!
This setup.py file is deprecated and will be removed in version 4.1.0
Please use pyproject.toml instead for modern Python packaging.
"""

import codecs
import os
import re
import warnings
from setuptools import setup, find_packages

# Show deprecation warning
warnings.warn(
    "\nDEPRECATION WARNING: setup.py installation is deprecated and will be removed in version 4.0.0.\n"
    "Please use pyproject.toml for installation. This is the modern way of Python packaging.",
    DeprecationWarning,
    stacklevel=2
)

def get_version():
    """Get version from __init__.py"""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(
        os.path.join(here, "invisible-chromedriver", "__init__.py"),
        mode="r",
        encoding="utf-8",
    ) as fp:
        try:
            return re.findall(r"^__version__ = ['\"]([^'\"]*)['\"]", fp.read(), re.M)[0]
        except Exception:
            raise RuntimeError("Unable to determine version.")

def get_long_description():
    """Get long description from README.md"""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        return f.read()

setup(
    name="invisible-chromedriver",
    version=get_version(),
    packages=find_packages(exclude=["tests*"]),
    package_data={
        "invisible-chromedriver": ["example/*.py"],
    },
    python_requires=">=3.9",
    install_requires=[
        "selenium>=4.9.0",
        "requests>=2.31.0",
        "websockets>=12.0",
        "playwright>=1.41.0",
        "asyncio>=3.4.3",
        "aiohttp>=3.9.0",
        "orjson"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.23.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
            "pytest-playwright>=0.4.0",
        ],
        "async": [
            "playwright>=1.41.0",
            "asyncio>=3.4.3",
            "aiohttp>=3.9.0",
        ],
    },
    url="https://github.com/Vadim-Khristenko/undetected-chromedriver",
    project_urls={
        "Bug Tracker": "https://github.com/Vadim-Khristenko/undetected-chromedriver/issues",
        "Source Code": "https://github.com/Vadim-Khristenko/undetected-chromedriver",
        "Documentation": "https://github.com/Vadim-Khristenko/undetected-chromedriver",
    },
    license="GPL-3.0",
    author="UltrafunkAmsterdam, Vadim Khristenko",
    author_email="info@blackhat-security.nl, via.by.vai@gmail.com",
    description="Selenium.webdriver.Chrome replacement with advanced anti-detection features and async support",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Testing",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Framework :: AsyncIO",
    ],
)
