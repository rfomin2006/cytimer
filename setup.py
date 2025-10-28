from setuptools import setup
from Cython.Build import cythonize

setup(
    name="cytimer",
    version="0.1.0",
    author="rfomi",
    author_email="rfomin2805@gmail.com",
    license="MIT",
    ext_modules=cythonize(
        "src/core.pyx",
        compiler_directives={"language_level": "3"}
    ),
    zip_safe=False,
)
