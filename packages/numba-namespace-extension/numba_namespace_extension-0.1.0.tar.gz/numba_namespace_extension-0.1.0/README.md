# Numba Namespace Extension

The idea of this package is to facilitate the creation of compiled numba extensions **without** 
modifying the original code implementation. The recommended approach is to use python namespaces so that
we can have the compiled version of the main package with the same access pattern. This looks like the following:

* Have the original package in a namespace module called `my_package`:

```commandline
$ pip install -e my_package
```

```python
from my_package.utils import my_function
```

```text
Simple main package configuration using `my_package` namespace.
├── setup.py
├── README.md
└── src
    └──my_package
        └── utils.py
```

* Create a compiled version of the functions of the original package, in an independent python package using the same
`my_pacakge` namespace.

```commandline
$ pip install -e my_package_compiled
```

```python
from my_package.compiled.utils import my_function
```

```text
Simple compiled package configuration using `my_package` namespace.
├── setup.py
├── README.md
├── registry.json
└── src
    └──my_package
        └── compiled
            └── __init__.py
```

By following the namespace suggestion, you can keep your original code in the `my_package` library and have an extra
independent python package with the compiled version but sharing the same access point (namespace).

Shared configuration between `my_package` and `my_package_compiled`:
* They both use a `my_package` namespace. In practice, this means that there's no `__init__.py` on under the
`my_package` directory.
* They are probably using the `setuptools.find_namespace_packages` function in the `setup.py` file.

Differences between the `my_package` and `my_package_compiled` implementations:
* The `my_package_compiled` library depends on already having the `my_pacakge` library installed.
* The `registry.json` file contains the information needed for the numba compiler (for each function).
* The `my_package_compiled` does not has custom-made code; only the compiled version of the functions defined in the
`registry.json` file.


**What are python namespace packages?** In short, namespace modules are like regular python modules but
without the `__init__.py` file. This allows you to share the same "module name" among different packages.
Consider the following example:

* Shared namespace: `my_package`
* Package 1 (`package-1`): Implement hello world in english
* Package 2 (`package-2`): Implement hello world in spanish

**Package 1**: contains a `hello_world.py` python submodule within the `my_package` namespace.

``` 
README.md
setup.py
src/
    my_package/
        hello_world.py
```

**Package 2**: contains a `hola_mundo.py` python submodule within the `my_package` namespace.

``` 
README.md
setup.py
src/
    my_package/
        hola_mundo.py
```

**Expected behavior**: you can install each package independently. Nonetheless, they will share a common namespace. 
Take a look at a complete working implementation [here](https://github.com/RHDZMOTA/python-namespace-example).

Learn more about namespace packages:
* In this [twitter thread](https://twitter.com/RHDZMOTA/status/1456338113983299584).
* From the [documentation](https://packaging.python.org/guides/packaging-namespace-packages/).

## Installation

You can install this package via `pip` by running:

```commandline
$ pip install numba_namespace_extension
```

Alternatively, for development installation, clone this repo and run:

```commandline
$ pip install -e .
```

## Usage

The suggested usage is to create a python package with a matching namespace to the library with the original code.
You can do this by manually creating the new package or leveraging our cookiecutter template with a minimal
python namespace package setup.

Install cookiecutter (i.e., `pip install cookiecutter`) and execute the template:

**(Option 1)** Referencing Github:

```commandline
cookiecutter https://github.com/RHDZMOTA/numba-namespace-extension.git
```

**(Option 2)** Or locally if you have this repo already cloned:

```commandline
cookiecutter path/to/repo
```

You can now start registering functions in the `registry.json` file. For each function, provide the following:
* `module (str)`: the module name where the original function is located.
* `function_name (str)`: the original function name.
* `signature`: the numba type signature (read more this [here](https://numba.pydata.org/numba-doc/dev/reference/types.html)).

Compilation is done when installing your package. You can install it locally by running:
* Replace `path/to/my_package` with the full or relative path to your package (i.e., directory where the `setup.py` is located).

```commandline
pip install -e path/to/my_package
```

Key components:
* The `Registry` class is basically a wrapper over the [Numba AOT](https://numba.pydata.org/numba-doc/dev/user/pycc.html)
  implementation that allows us to define source functions on the configuration file (i.e., `registry.json`)
* Use the `from_json` static method to create a `Registry` instance referencing the json config file.
* Once you have an instance, run the `ext_modules` and pass the result to the `ext_modules` argument from the `setup` function.
* Consider that all the modules referenced by the `registry.json` file MUST be available in the installation runtime.

Example of minimal `setup.py` file:

```python
from setuptools import setup, find_namespace_packages
from numba_namespace_extension.registry import Registry

setup(
    name="<package-name>",
    version="0.1.0",
    packages=find_namespace_packages(where="src"),
    package_dir={
        "": "src"
    },
    ext_modules=Registry.from_json("registry.json").ext_modules()
)

```
