project = "Sphinx pyOpenSci Theme"
copyright = "2024"
author = "pyOpenSci"
master_doc = "index"
version = "0.0.1a"

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

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pyos_sphinx_theme"
html_title = "pyOpenSci Sphinx Theme"
html_copy_source = True
html_sourcelink_suffix = ""

# Opengraph configuration
# ref: https://sphinxext-opengraph.readthedocs.io/en/latest/index.html
#
ogp_site_url = "https://sphinx-2i2c-theme.readthedocs.io/en/latest/"
ogp_social_cards = {
    "site_url": "pyopensci.org",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]


# html_theme_options = {
#     "path_to_docs": "docs",
#     "repository_url": "https://github.com/2i2c-org/sphinx-2i2c-theme",
#     "use_edit_page_button": True,
#     "use_issues_button": True,
#     "use_download_button": True,
# }

html_context = {
    "github_user": "pyopensci",
    "github_repo": "pyos-sphinx-theme",
    "github_version": "main",
    "doc_path": "docs",
}