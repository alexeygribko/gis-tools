import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires=[
   'matplotlib==3.1.3',
   'folium==0.12.1',
   'pandas==1.1.5',
   'geopandas==0.9.0',
   'descartes==1.1.0',
   'scikit-learn>=0.22.2',
   'geopy==1.17.0'
]

setuptools.setup(
    name="gis-tools",
    version="0.0.3",
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
    install_requires=install_requires,
    python_requires=">=3.7.1",
)