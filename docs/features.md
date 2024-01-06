# Extra features in this theme

## Embed videos on Google Drive

You can **embed videos hosted in Google Drive** with this theme.

**Embed Google Drive videos** by uploading it to Google Drive, right-clicking it, click `Get link`, and click `🔗 Copy link`.
Paste the link into the `{video}` directive.
For example:

````
```{video} https://drive.google.com/file/d/1vtr54KvM7Vr01wZ1uz0bOrpDvnMGmKy8/view?usp=share_link
```
````

Results in:

```{video} https://drive.google.com/file/d/1vtr54KvM7Vr01wZ1uz0bOrpDvnMGmKy8/view?usp=share_link
```

**Embed youtube videos** by using the URL of the video you wish to embed (not the "share" link).
For example:

````
```{video} https://www.youtube.com/watch?v=lZ2FHTkyaMU&t=13s
```
````

Results in:

```{video} https://www.youtube.com/watch?v=lZ2FHTkyaMU&t=13s
```

## Header links

It adds a header that provides site-wide links across all of our documentation.

## CSS and visual style

We download the "Poppins" and "Itim" fonts from Google Fonts and embed it in our side, since this is what our logo uses.

We also define several custom CSS rules to handle a header with cross-organization links.

## Redirect to `dirhtml`

2i2c's documentation uses the `dirhtml` builder so that links look like `mysite.org/pagename` instead of `mysite.org/pagename.html`.[^1]
However, the Sphinx default uses the `html` builder, and our documentation often has historical links from earlier iterations where we used the `html` builder.

[^1]: In practice, this creates a file at `pagename/index.html`.
      When a user visits `mysite.org/pagename`, the browser tells you it is a directory.
      By default, browsers will then look for an `index.html` file in that directory and display it.
      This function creates _another_ file at `pagename.html` and makes it redirect to `pagename/`, and thus displays `pagename/index.html`.

To avoid broken links, this theme includes a helper event callback that does two things:

- If `dirhtml` is the builder, create files so that `pagename.html` redirects to `pagename`.
  This ensures that old `html` builder links redirect.
- If `html` is the builder, raise a warning that the `dirhtml` builder should be used instead.

## Extensions

**`sphinxext.opengraph`** adds OpenGraph tags to each of our sites.
It also pre-configures the social media cards to use `2i2c.org`.

**`sphinx-togglebutton`** allows us to make admonitions toggle-able with `:class: dropdown`.

**`sphinx-copybutton`** adds a copy button to each of our code blocks.
