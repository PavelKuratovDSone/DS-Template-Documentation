
import sphinx
import sphinx_rtd_theme
import sys
import os

needs_sphinx = "1.3"

sys.path.append(os.path.abspath("_extensions"))
extensions = [
    
]

sphinx_tabs_nowarn = True

templates_path = ['_templates']


source_suffix = ".rst"
source_encoding = "utf-8-sig"


master_doc = 'index'


project = u'DSone HC Template Documentation'
copyright = u'2022 DSone'


version = '1.0'

release = version


exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Theme options
html_theme_options = {
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
}

html_static_path = ['_static']

html_css_files = [
    'css/algolia.css',
    'https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css',
    "css/custom.css",
]
html_js_files = [
    "js/custom.js",
    ('https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.js', {'defer': 'defer'}),
    ('js/algolia.js', {'defer': 'defer'})
]





htmlhelp_basename = 'DSone HC Template Documentation'



man_pages = [
    ('index', 'DSone HC Template Documentation', u'Read the DSone HC Template Documentation',
     [u'Read the Docs'], 1)
]




