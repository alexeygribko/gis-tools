import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gis-tools",
    version="0.0.1",
    author="Alexey Gribko",
    author_email="agribko@sheeva.ai",
    description="Functions for GIS data processing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexeygribko/gis-tools",
    project_urls={
        "Bug Tracker": "https://github.com/alexeygribko/gis-tools/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7.5",
)