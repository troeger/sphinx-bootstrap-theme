"""Sphinx bootstrap theme."""
import os

VERSION = (0, 6, 2)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__

def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return [theme_path]

def setup(app):
    """Setup."""
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, 'add_html_theme'):
        theme_path = get_html_theme_path()
        app.add_html_theme('bootstrap', os.path.join(theme_path, 'bootstrap'))
