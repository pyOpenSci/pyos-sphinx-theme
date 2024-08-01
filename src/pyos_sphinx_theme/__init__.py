"""A lightweight theme for pyOpenSci."""
from pathlib import Path
# from sphinx_book_theme import hash_assets_for_files
from sphinx.util import logging

from pydata_sphinx_theme.utils import config_provided_by_user

# disable the video directive and html2dirhtml redirection because they are not implemented yet with this theme
from .video import Video # activate this line to enable the video directive
from .html2dirhtml import redirect_from_html_to_dirhtml # nactivate this line to enable the html2dirhtml redirection

__version__ = "0.0.1dev0"
LOGGER = logging.getLogger(__name__)

THIS_PATH = Path(__file__).parent.resolve()
THEME_PATH = THIS_PATH / "theme" / "pyos_sphinx_theme"
LOGO_LIGHT = str((THEME_PATH / "static" / "images" / "logo-light-mode.png").absolute()).replace("\\", "/")
LOGO_DARK = str((THEME_PATH / "static" / "images" / "logo-dark-mode.png").absolute()).replace("\\", "/")

PYOPENSCI_LOGO_PACKAGE_GUIDE = str((THEME_PATH / "static" / "images" / "pyopensci-logo-package-guide.png").absolute()).replace("\\", "/")
PYOPENSCI_PYTHON_PACKAGE_GUIDE = str((THEME_PATH / "static" / "images" /"pyopensci-python-package-guide.png").absolute()).replace("\\", "/")

def update_config(app):
    # These are the theme options that will be used in the build
    theme_options = app.config.html_theme_options

    # add icons to the navbar
    if "icon_links" not in theme_options:

        theme_options["icon_links"] =[
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@pyOpenSci",
            "icon": "fa-brands fa-mastodon",
        },
    ]

    if "external_links" not in theme_options:
        theme_options["external_links"] = [
        {
            "url": "https://www.pyopensci.org",
            "name": "pyOpenSci Website",
        },
        {
            "url": "https://www.pyopensci.org/software-peer-review",
            "name": "Peer Review Guide",
        },
        {
            "url": "https://pyopensci.org/handbook",
            "name": "Handbook",
        },
    ]

    if not "logo" in theme_options:
        theme_options["logo"] = {
            "image_dark": LOGO_DARK,
            "image_light": LOGO_LIGHT
    }

    if not "header_links_before_dropdown" in theme_options:
        theme_options["header_links_before_dropdown"] = 4

    # Social previews config
    social_cards = app.config.__dict__.get("ogp_social_cards", {})
    
    app.config.ogp_site_name = "pyOpenSci Python Package Guide"
    app.config.ogp_social_cards = {
        "line_color": "#6D597A",
        "image": "_static/pyopensci-logo-package-guide.png",
    }

    # If no html_logo is set then use a stock 2i2c logo
    if not config_provided_by_user(app, "html_logo") and not social_cards.get("image"):
        line_color = "#6D597A"
        social_cards["image"] = str(LOGO_LIGHT)
        social_cards["line_color"] = line_color

    app.config.ogp_social_cards = social_cards


def activate_extensions(app, extensions):
    """Activate extensions bundled with this theme.

    This also manually triggers the `config-inited` build step to account for
    added extensions that hook into this event.
    """

    # Remove all of the `config-inited` event listeners because they've already triggered
    # We'll then re-trigger this event after adding extensions so that *only* their event hooks trigger
    old_listeners = app.events.listeners["config-inited"]
    app.events.listeners["config-inited"] = []

    # Activate a few extensions by default
    for extension in extensions:
        # If it's already been activated just skip it
        if extension in app.config.extensions:
            continue
        app.setup_extension(extension)

    # Emit the config-inited event so that the new extensions run their hooks
    app.emit("config-inited", app.config)

    # Finally join back the lists
    app.events.listeners["config-inited"][:0] = old_listeners


def setup(app):
    app.add_html_theme("pyos_sphinx_theme", THEME_PATH)
    app.config.html_favicon = "https://www.pyopensci.org/images/favicon.ico"
    app.connect("builder-inited", update_config)
    # app.connect("html-page-context", redirect_from_html_to_dirhtml)
    # app.add_css_file("static/styles/pyos-sphinx-theme.css")
    # app.add_js_file("static/scripts/matomo.js")
    app.add_css_file("https://fonts.googleapis.com/css2?family=Itim&family=Poppins:wght@400;700&family=Work+Sans:wght@400;700")
#     activate_extensions(app, add_extensions)

    # Video directive
    # app.add_directive("video", Video)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
