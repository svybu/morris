from setuptools import setup, find_namespace_packages

setup(name='topwords',
      version='0.0.1',
      description='Python library to extract the most common word combinations from a text',
      # url='',
      author='svibu',
      author_email='svibu.dev@gmail.com',
      # license= ,
      packages=find_namespace_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      install_requires=['nltk==3.7']
      )
