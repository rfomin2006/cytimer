from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name="cytimer",
    version="0.1.0",
    author="rfomi", 
    author_email="rfomin2805@gmail.com",
    license="MIT",
    setup_requires=["cython>=3.1"],
    ext_modules=cythonize(
        Extension("cytimer", ["src/core.pyx"]),
        compiler_directives={"language_level": "3"}
    ),
    zip_safe=False,
)