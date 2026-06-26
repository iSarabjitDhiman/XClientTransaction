from setuptools import setup, find_packages

VERSION = "1.0.3"
SHORT_DESCRIPTION = "Twitter X-Client-Transaction-Id generator written in python."

with open("requirements.txt") as file:
    dependencies = file.read().splitlines()
with open("README.md", "r") as file:
    DESCRIPTION = file.read()


setup(
    name="xclienttransaction",
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Sarabjit Dhiman",
    author_email="hello@sarabjitdhiman.com",
    license="MIT",
    url="https://github.com/iSarabjitDhiman/XClientTransaction",
    packages=find_packages(),
    keywords=["XClientTransaction", "twitter transaction id", "client transaction id twitter",
              "tid generator", "x client transaction id generator",
              "xid twitter", "tweeterpy"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
    ],
    install_requires=dependencies,
    python_requires=">=3"
)
