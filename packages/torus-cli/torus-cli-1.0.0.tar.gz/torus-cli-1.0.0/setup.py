import setuptools

setuptools.setup(
    name="torus-cli",
    version="1.0.0",
    author="Luca Albinati",
    author_email="luca.albinati@gmail.com",
    description="Command line interface for torus-engine",
    url="https://github.com/lucaalbinati/torus-cli",
    project_urls={
        "Bug Tracker": "https://github.com/lucaalbinati/torus-cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)