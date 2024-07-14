from sphinx.util import logging
from pathlib import Path

LOGGER = logging.getLogger(__name__)

REDIRECT_TEMPLATE = """
<html>
    <head>
        <noscript>
            <meta http-equiv="refresh" content="0; url={rel_url}"/>
        </noscript>
    </head>
    <body>
        <script>
            window.location.href = '{rel_url}' + (window.location.search || '') + (window.location.hash || '');
        </script>
        <p>You should have been redirected.</p>
        <a href="{rel_url}">If not, click here to continue.</a>
    </body>
</html>
"""

def redirect_from_html_to_dirhtml(app, pagename, templatename, context, doctree):
    """If dirhtml builder is used, redirect pagename.html to the directory `pagename`"""
    if not hasattr(app, "builder"):
        return
    if app.builder.name == "dirhtml":
        # Assume that "pagename.html" needs to redirect to pagename/index.html"
        path_html = (Path(app.outdir) / pagename).with_suffix(".html")
        page_folder = pagename.split("/")[-1]

        # Create the direct directory and write a new index.html file
        path_html.parent.mkdir(exist_ok=True, parents=True)
        path_html.write_text(REDIRECT_TEMPLATE.format(rel_url=page_folder))

        LOGGER.info(f"Redirecting {pagename}.html to {pagename}")

    elif app.builder.name == "html":
        LOGGER.warn("Use the dirhtml builder instead of html builder!")