# Develop this theme

## Theme build system

This theme uses the [`sphinx-theme-builder` tool](https://github.com/pradyunsg/sphinx-theme-builder), which is a helper tool for automatically compiling Sphinx theme assets.
This will download a local copy of NodeJS and build the theme's assets with the environment specified in `package.json`.

## Theme structure

This theme follows the [`sphinx-theme-builder` filesystem layout](https://sphinx-theme-builder.readthedocs.io/en/latest/filesystem-layout/).

## clone the repository

To develop this theme, clone the repository and install the dependencies:

```bash
git clone https://github.com/pyOpenSci/pyos-sphinx-theme.git
cd pyos-sphinx-theme
pip install -e .[dev]
```

## Build the theme locally

You can build the documentation for this theme to preview it.
The easiest way to build the documentation in this repository is to use [the `nox` automation tool](https://nox.thea.codes/), a tool for quickly building environments and running commands within them.
This ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox`

   ```console
   $ pip install nox
   ```
2. Build the documentation:

   ```console
   $ nox -s docs
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `docs/_build/html`.

To build live documentation that updates when you update local files, run the following command:

```console
$ nox -s docs -- live
```
