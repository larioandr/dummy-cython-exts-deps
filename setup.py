from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

extensions = [
    Extension(
        "dummy.core.py_core", [
            "dummy/core/py_core.pyx", 
            "cpp_src/core/core.cpp"
        ], include_dirs=["cpp_src"], language="c++"),
    Extension(
        "dummy.app.py_app", [
            "dummy/app/py_app.pyx",
            "cpp_src/app/app.cpp",
        ], include_dirs=["cpp_src"], language="c++"),
]

setup(name="dummy", version="1.0", packages=find_packages(), zip_safe=False,
      ext_modules=cythonize(extensions))
