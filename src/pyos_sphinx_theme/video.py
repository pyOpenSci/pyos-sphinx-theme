"""Allows us to embed Google Drive videos into our docs.
"""
from docutils.parsers.rst import Directive
from docutils import nodes
from docutils.parsers.rst.directives import positive_int

IFRAME_TEMPLATE = '<iframe width="{width}" height="{height}" src="{src}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'

class Video(Directive):
    arguments = 1
    final_argument_whitespace = False
    has_content = True

    option_spec = {"width": positive_int, "height": positive_int}

    def run(self):
        link = self.content[0]
        # Video window defaults to a 16:9 ratio
        width = self.options.get("width", 533)
        height = self.options.get("height", 300)

        # If Drive link, parse the "share" link and insert its UID into an iframe
        # Link ref: https://drive.google.com/file/d/1vtr54KvM7Vr01wZ1uz0bOrpDvnMGmKy8/view?usp=share_link
        if "drive.google.com/file" in link:
            uid = link.split("/d/")[-1].split("/")[0]
            iframe = IFRAME_TEMPLATE.format(width=width, height=height, src=f"https://drive.google.com/file/d/{uid}/preview")
        # Youtube
        # Link ref: https://www.youtube.com/watch?v=dQw4w9WgXcQ
        elif "youtube.com" in link:
            uid = link.split("v=")[-1]
            # In case there were other arguments after the video link
            uid = uid.split("&")[0]

            iframe = IFRAME_TEMPLATE.format(width=width, height=height, src=f"https://www.youtube.com/embed/{uid}")
        else:
            raise ValueError(f"Unidentified video link: {link}")
        
        # Use a raw pass-through node
        para = nodes.raw("", iframe, format="html")
        return [para]
 