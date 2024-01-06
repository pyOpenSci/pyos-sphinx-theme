# The pyOpenSci documentation theme

A lightweight theme built on the Sphinx Book Theme, for use by 2i2c.
It makes minimal changes to the `sphinx-book-theme` in order to standardize a top-bar that can be shared across all 2i2c documentation.

It does these two primary things:

- Overrides the `layout.html` template so that we include a topbar of links and a standard footer.
- Adds some CSS that standardizes the look and feel according to 2i2c colors

Other than this, the theme behaves the exact same as the [sphinx book theme](https://sphinx-book-theme.readthedocs.io).

## User guide

These have sections about using this theme

```toctree
:hidden:

features
use
develop
showcase
```

## Reference

See the kitchen sink for some example pages.

```{toctree}
:maxdepth: 3
reference/kitchen-sink/index
```