from setuptools import setup, find_packages
import os

version = '0.0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.formcriteria.numfield',
      version=version,
      description="Extention for collective.formcriteria",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Bogdan Girman',
      author_email='bogdan.girman@gmail.com',
      url='http://girman.in.ua',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.formcriteria'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.formcriteria',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
