"""pyOpenSci Sphinx Theme configuration."""

from pyos_sphinx_theme import __version__

project = "pyOpenSci Sphinx Theme"
copyright = "2024"
author = "pyOpenSci"
master_doc = "index"
version = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "pyos_sphinx_theme"
html_title = project
html_copy_source = True
html_sourcelink_suffix = ""

html_static_path = ["_static"]

html_theme_options = {
    "github_url": "https://github.com/pyOpenSci/pyos-sphinx-theme",
    "use_edit_page_button": True,
}

html_context = {
    "github_user": "pyopensci",
    "github_repo": "pyos-sphinx-theme",
    "github_version": "main",
    "doc_path": "docs",
}
