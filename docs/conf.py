# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Test Project'
copyright = '2022, Sachin'
author = 'Sachin'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_multiversion'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

#html_sidebars = [
#    "_templates/versioning.html",
#]

html_sidebars = {'**': ['versioning.html']}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

#smv_remote_whitelist = None
#smv_remote_whitelist = r"^upstream$"
smv_remote_whitelist = r'^.*$'
#smv_branch_whitelist = r'^(?!master).*$'