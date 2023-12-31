import setuptools

setuptools.setup(
    name="test_package",
    description="MyDescription",
    long_description="MyLongDescription",
    long_description_content_type="text/markdown",
    license="Apcahe 2.0",
    url="https://davidvonthenen.com",
    author="David vonThenen",
    author_email="davidvonthenen@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    keywords="my test package",
    packages=setuptools.find_packages(),
    install_requires=[],
)
