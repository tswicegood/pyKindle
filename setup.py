from distutils.core import setup

import kindle

# TODO: add classifiers
setup(
    name = "pyKindle",
    version = kindle.__version__,
    packages = ["kindle", ],
    author = "Travis Swicegood",
    author_email = "development@domain51.com"
)
