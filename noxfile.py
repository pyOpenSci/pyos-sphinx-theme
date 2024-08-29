"""Build and preview this theme documentation locally.

To build with a live-server:

    nox -s docs -- live

To re-install dependencies:

    nox -s docs -- -r
"""

import pathlib

import nox

nox.options.reuse_existing_virtualenvs = True

## Sphinx related options

# Sphinx output and source directories
SOURCE_DIR = pathlib.Path("docs")
BUILD_DIR = pathlib.Path("_build")
OUTPUT_DIR = pathlib.Path(BUILD_DIR, "html")

nox.options.reuse_existing_virtualenvs = True

# Sphinx build commands
SPHINX_BUILD = "sphinx-build"
SPHINX_AUTO_BUILD = "sphinx-autobuild"

# Sphinx parameters used to build the guide
BUILD_PARAMETERS = ["-b", "html"]

# Sphinx parameters used to test the build of the guide
TEST_PARAMETERS = ["-W", "--keep-going", "-E", "-a"]

AUTOBUILD_IGNORE = [
    "_build",
    ".nox",
    "build_assets",
    "tmp",
]


@nox.session
def docs(session):
    """Build the packaging guide."""
    session.install("-e", ".")
    session.run(SPHINX_BUILD, *BUILD_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs)


@nox.session(name="docs-live")
def docs_live(session):
    """Build and launch a local copy of the guide.

    This session will use sphinx-autobuild to build the guide and launch a local server so you can
    browse it locally. It will automatically rebuild the guide when changes are
    detected in the source.

    It can be used with the language parameter to build a specific translation, for example:

        nox -s docs-live -- -D language=es

    Note: The docs-live-lang session below is provided as a convenience session for beginner
    contributors. so they don't need to remember the specific sphinx-build parameters to
    build a different language.
    """
    session.install("-e", ".")
    cmd = [SPHINX_AUTO_BUILD, *BUILD_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    # This part was commented in the previous version of the nox file, keeping the same here
    # for folder in AUTOBUILD_INCLUDE:
    #     cmd.extend(["--watch", folder])
    session.run(*cmd)


@nox.session(name="docs-test")
def docs_test(session):
    """Build the packaging guide with more restricted parameters.

    Note: this is the session used in CI/CD to release the guide.
    """
    session.install("-e", ".")
    session.run(
        SPHINX_BUILD, *BUILD_PARAMETERS, *TEST_PARAMETERS, SOURCE_DIR, OUTPUT_DIR, *session.posargs
    )


@nox.session(name="linkcheck")
def linkcheck(session):
    """Check the links in the documentation."""
    session.install("-e", ".")
    session.run(
        SPHINX_BUILD,
        *BUILD_PARAMETERS,
        "-b",
        "linkcheck",
        SOURCE_DIR,
        OUTPUT_DIR,
        *session.posargs,
    )
