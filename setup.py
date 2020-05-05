import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptopay",
    version="0.1.1",
    author="Peter Gonda",
    author_email="peter@pipoline.com",
    description="Crypto.com pay module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pipoline/cryptopay",
    packages=setuptools.find_packages(),
    license="MIT",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
