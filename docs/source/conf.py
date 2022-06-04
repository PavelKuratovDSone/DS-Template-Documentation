
import sphinx
import sphinx_rtd_theme
import sys
import os

needs_sphinx = "1.3"

sys.path.append(os.path.abspath("_extensions"))
extensions = [
    "sphinx_tabs.tabs",
    "notfound.extension",
    "sphinxext.opengraph",
]

sphinx_tabs_nowarn = True

templates_path = ['_templates']


source_suffix = ".rst"
source_encoding = "utf-8-sig"


master_doc = 'index'


project = u'Read the Docs Template'
copyright = u'2014, Read the Docs'


version = '1.0'

release = version


exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'ReadtheDocsTemplatedoc'



man_pages = [
    ('index', 'readthedocstemplate', u'Read the Docs Template Documentation',
     [u'Read the Docs'], 1)
]

texinfo_documents = [
  ('index', 'ReadtheDocsTemplate', u'Read the Docs Template Documentation',
   u'Read the Docs', 'ReadtheDocsTemplate', 'One line description of project.',
   'Miscellaneous'),
]


