from .py_core cimport greet as cpp_greet

def call_greet():
    cpp_greet()
