"""A lightweight theme for pyOpenSci."""
from pathlib import Path
# from sphinx_book_theme import hash_assets_for_files
from sphinx.util import logging

from pydata_sphinx_theme.utils import get_theme_options_dict, config_provided_by_user
from .video import Video
from .html2dirhtml import redirect_from_html_to_dirhtml

__version__ = "0.0.1"
LOGGER = logging.getLogger(__name__)

THEME_PATH = (Path(__file__).parent / "theme" / "sphinx-2i2c-theme").resolve()


def update_config(app):
    # These are the theme options that will be used in the build
    theme_options = app.config.html_theme_options
    
    # If no URL is set, don't generate social previews
    if not config_provided_by_user(app, "ogp_site_url"):
        app.config.ogp_site_url = "2i2c.org"

    # Social previews config
    social_cards = app.config.__dict__.get("ogp_social_cards", {})

    # If no html_logo is set then use a stock 2i2c logo
    if not config_provided_by_user(app, "html_logo") and not social_cards.get("image"):
        path_static = Path(__file__).parent / "theme/sphinx-2i2c-theme/static"
        path_img = path_static / "images/logo.png"
        social_cards["image"] = str(path_img)

    app.config.ogp_social_cards = social_cards

    # Add icon links to config
    icon_links = [
        {
            "name": "Twitter",
            "url": "https://twitter.com/2i2c_org",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "Mastodon",
            "url": "https://hachyderm.io/@2i2c_org",
            "icon": "fa-brands fa-mastodon",
            # This allows us to verify this page in Mastodon
            "attributes": {
               "rel" : "me",
            },
        },
        {
            "name": "Contact",
            "url": "https://2i2c.org/#contact",
            "icon": "fas fa-envelope",
        },
        {
            "name": "Blog",
            "url": "https://2i2c.org/blog",
            "icon": "fas fa-newspaper",
        },
    ]
    if "icon-links" not in theme_options:
        theme_options["icon_links"] = icon_links


def hash_html_assets(app, pagename, templatename, context, doctree):
    assets = ["styles/sphinx-2i2c-theme.css"]
    # hash_assets_for_files(assets, THEME_PATH / "static", context, app)


# def activate_extensions(app, extensions):
#     """Activate extensions bundled with this theme.
    
#     This also manually triggers the `config-inited` build step to account for
#     added extensions that hook into this event.
#     """

#     # Remove all of the `config-inited` event listeners because they've already triggered
#     # We'll then re-trigger this event after adding extensions so that *only* their event hooks trigger
#     old_listeners = app.events.listeners["config-inited"]
#     app.events.listeners["config-inited"] = []

#     # Activate a few extensions by default
#     for extension in extensions:
#         # If it's already been activated just skip it
#         if extension in app.config.extensions:
#             continue
#         app.setup_extension(extension)

#     # Emit the config-inited event so that the new extensions run their hooks
#     app.emit("config-inited", app.config)

#     # Finally join back the lists
#     app.events.listeners["config-inited"][:0] = old_listeners


def setup(app):
    app.add_html_theme("sphinx_2i2c_theme", THEME_PATH)
    app.config.html_favicon = "https://2i2c.org/media/icon.png"
    app.connect("builder-inited", update_config)
    app.connect("html-page-context", hash_html_assets)
    app.connect("html-page-context", redirect_from_html_to_dirhtml)

    # Add our folder for templates
    here = Path(__file__).parent.resolve()
    theme_path = here / "theme" / "sphinx-2i2c-theme"
    app.config.templates_path.append(str(theme_path / "components"))

    # Use the Google Fonts CDN to quickly load our fonts
    # ref: https://developers.google.com/fonts/docs/css2
    app.add_css_file("https://fonts.gstatic.com", rel="preconnect")
    app.add_css_file("https://fonts.googleapis.com/css2?family=Itim&family=Poppins:wght@400;700&family=Work+Sans:wght@400;700")
    # add_extensions = ["sphinx_copybutton", 
    #                   "sphinx_togglebutton", 
    #                   "sphinxext.opengraph", 
    #                   "sphinx.ext.intersphinx", 
    #                   "sphinx_design", 
    #                   "sphinx_sitemap",]
    # activate_extensions(app, add_extensions)

    # Video directive
    # app.add_directive("video", Video)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
