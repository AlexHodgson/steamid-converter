import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="steamid-converter-ALEX-HODGSON", # Replace with your own username
    version="0.0.1",
    author="Alex Hodgson",
    author_email="alex.hodgson@sci-fact.com",
    description="For easy conversion between steamID formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)