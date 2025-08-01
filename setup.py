#!/usr/bin/env python3
"""
Setup script for Record Shelf
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Development requirements
dev_requirements = [
    'pytest>=7.0.0',
    'pytest-cov>=4.0.0',
    'pylint>=2.15.0',
    'black>=22.0.0',
    'isort>=5.10.0',
    'mypy>=1.0.0',
    'tox>=4.0.0',
    'build>=0.8.0',
    'twine>=4.0.0',
]

setup(
    name="discogs-record-shelf",
    version="1.0.3",
    author="Bryan Kemp",
    author_email="bryan@kempville.com",
    description="A tool for creating custom reports from music collection data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bryankemp/discogs-record-shelf",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "record-shelf=record_shelf.cli:main",
        ],
    },
    keywords="music collection report excel csv shelf organize",
    project_urls={
        "Bug Reports": "https://github.com/bryankemp/discogs-record-shelf/issues",
        "Source": "https://github.com/bryankemp/discogs-record-shelf",
        "Documentation": "https://discogs-record-shelf.readthedocs.io/",
    },
    include_package_data=True,
    zip_safe=False,
)

