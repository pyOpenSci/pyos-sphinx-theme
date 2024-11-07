# Develop this theme

## Theme build system

This theme uses the [`sphinx-theme-builder` tool](https://github.com/pradyunsg/sphinx-theme-builder), which is a helper tool for automatically compiling Sphinx theme assets.
This will download a local copy of NodeJS and build the theme's assets with the environment specified in `package.json`.

## Theme structure

This theme follows the [`sphinx-theme-builder` filesystem layout](https://sphinx-theme-builder.readthedocs.io/en/latest/filesystem-layout/).

## Create a new development environment

### Using Conda or Mamba

1. If you are a conda or mamba user, create a new environment  

Note: Mamba is a faster alternative to `conda`.

```bash
mamba create -n pyos_sphinx python=3.10
mamba activate pyos_sphinx
```

### 1.Create a venv Environment with Python 3.10

Alternatively you could create a venv environment.
To create a virtual environment named my_env, run:

```bash
python3.10 -m venv my_env
# Activate on mac / linux
source my_env/bin/activate
```

### 2. Clone the repository

To develop this theme locally, clone the repository and install the
dependencies:

```bash
git clone https://github.com/pyOpenSci/pyos-sphinx-theme.git
cd pyos-sphinx-theme
```

### Install the theme in editable mode with development dependencies

```
pip install -e ".[dev]"
```

## Build the theme locally

You can build the documentation for this theme to preview it.
The easiest way to build the documentation in this repository is to use [the `nox` automation tool](https://nox.thea.codes/), a tool for quickly building environments and running commands within them.
This ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox` using either pip or pipx.

```console
pip install nox
```

or

```console
pipx install nox
```

2. Build the documentation:

```console
nox -s docs
```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `docs/_build/html`.

To build live documentation that updates when you update local files, run the following command:

```console
nox -s docs-live
```

## Publish and release workflow

To build the theme's distribution files run:

```bash
hatch build
```

Hatch will store the build distribution files in the `dist/` directory of the cloned repo.

## Making a release

Currently we are using a manual versioning process where you need to
update the version of the package in our `__init__.py` file. Please
be sure to do this before cutting a new release on GitHub.

Once you have updated the version of the package, you are ready to make a release on GitHub.

A new tagged release will push the newly built theme to PyPI.
