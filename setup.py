from setuptools import setup, find_packages

setup(
    name="geometry-lib",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Dmitry Rzhanykh",
    author_email="ryedmitr@gmail.com",
    description="A Python library for geometric calculations",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dimarye/geometry-lib",
    project_urls={
        "Bug Tracker": "https://github.com/dimarye/geometry-lib/issues",
        "Source": "https://github.com/dimarye/geometry-lib",
        "Changelog": "https://github.com/dimarye/geometry-lib/releases",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
