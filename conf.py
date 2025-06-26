# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Home Depot MyCard Help'
copyright = '2025, Home Depot MyCard Help'
author = 'Home Depot MyCard Help'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = []

# Allow raw HTML blocks in .rst files
suppress_warnings = ['raw-html']
raw_enabled = True

# List of patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Fix Home Depot MyCard Login Issues – Step-by-Step Guide"

# Optional short title (e.g., for nav bar or header)
html_short_title = "Home Depot MyCard Login Help"

# Favicon (make sure 'favicon.ico' exists in _static or root)
html_favicon = 'favicon.ico'

# Choose a theme
# html_theme = 'sphinx_rtd_theme'  # A clean, widely used theme for documentation

# Theme customization options
html_theme_options = {
    'display_version': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'style_nav_header_background': '#FF6F00',  # Home Depot orange
    'navigation_depth': 3,
}

# Paths for templates and static files (uncomment if needed)
# templates_path = ['_templates']
# html_static_path = ['_static']
