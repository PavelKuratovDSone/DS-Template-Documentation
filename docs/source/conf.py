
import sphinx
import sphinx_rtd_theme
import sys
import os


extensions = []


templates_path = ['_templates']


source_suffix = '.rst'


master_doc = 'index'


project = u'Read the Docs Template'
copyright = u'2014, Read the Docs'


version = '1.0'

release = '1.0'


exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'ReadtheDocsTemplatedoc'



latex_elements = {
latex_documents = [
  ('index', 'ReadtheDocsTemplate.tex', u'Read the Docs Template Documentation',
   u'Read the Docs', 'manual'),
]

man_pages = [
    ('index', 'readthedocstemplate', u'Read the Docs Template Documentation',
     [u'Read the Docs'], 1)
]

texinfo_documents = [
  ('index', 'ReadtheDocsTemplate', u'Read the Docs Template Documentation',
   u'Read the Docs', 'ReadtheDocsTemplate', 'One line description of project.',
   'Miscellaneous'),
]


