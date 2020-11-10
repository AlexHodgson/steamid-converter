import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="steamid-converter",
    version="1.0.0",
    author="Alex Hodgson",
    author_email="alex.hodgson@sci-fact.com",
    description="Package for easy conversion between steamID formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexHodgson/steamid-converter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)