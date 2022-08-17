import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MailGw Temporary Email",
    version="0.0.2",
    author="bontoutou",
    description="10 Minute Temporary Email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['mail', 'email', 'temporary mail', 'temporary email', 'mailgw'],
    url="https://github.com/bontoutou00/MailGw",
    project_urls={
        "Bug Tracker": "https://github.com/bontoutou00/MailGw/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['requests']
)
