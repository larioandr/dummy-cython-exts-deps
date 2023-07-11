# dummy-cython-exts-deps
An example of building extensions for multiple C++ libraries depending on each other

Demonstrates the problem of building extensions for two libraries (`core` and `app`),
where `app` uses API of `core`.

Code of a C++ library is in `cpp_src`, python package is in `dummy`.

## Install

Instructions for building on Linux:

```
python3 -m venv .venv  # or create venv using your favourite tool
./.venv/bin/pip install cython
./.venv/bin/pip install -e .
```

## Problem demonstration

The package `dummy` has two extensions:

- `py_core`: wraps `cpp_src/core` (`libcore`)
- `py_app`: wraps `cpp_src/app` (`libapp`)

Calling `py_core` is ok:

```bash
./.venv/bin/python -c "from dummy.core.py_core import call_greet; call_greet()"
Hello from core
```

While calling `py_app` is not:

```bash
/.venv/bin/python -c "from dummy.app.py_app import get_the_answer; print(get_the_answer())"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: /***/dummy-cython-exts-deps/dummy/app/py_app.cpython-310-x86_64-linux-gnu.so: undefined symbol: _Z14someServiceFunv
```

