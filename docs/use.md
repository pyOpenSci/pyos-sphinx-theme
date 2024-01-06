# Use this theme

To use this theme in a repository, follow these steps:

- Add this theme to the `pip` install requirements of the repo. For now, point it to the `main` branch like so:

  ```
  # in requirements.txt
  git+https://github.com/2i2c-org/sphinx-2i2c-theme
  ```
  
  or to install locally
  
  ```console
  $ pip install git+https://github.com/2i2c-org/sphinx-2i2c-theme
  ```
- Configure the Sphinx docs to use the theme by editing `conf.py`

  ```python
  html_theme = "sphinx_2i2c_theme"
  ```
  
- Make any customizations that you wish, following the [sphinx book theme documenation](https://sphinx-book-theme.readthedocs.io).
