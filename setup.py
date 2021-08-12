from distutils.core import setup

setup(
    name="divisivlelist",
    packages=["divisiblelist"],
    version="0.2",
    license="gpl-3.0",
    description="Customizes 'UserList' to support spliting with / operator.",
    long_description=open("README.md").read(),
    author="Giovanni Nunes",
    author_email="giovanni.nunes@gmail.com",
    url="https://github.com/plainspooky/divisiblelist",
    keywords=["console", "terminal", "user interface"],
    install_requires=[],
    project_urls={
        "Documentation": "https://plainspooky.github.io/divisiblelist/index.html",
        "Source Code": "https://github.com/plainspooky/divisiblelist",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
