from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='pokedatabase_SDK',
  version='0.0.1',
  description='Pokemon information SDK',
  long_description=open('README.md').read() + '\n\n' + open('LICENSE.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type = 'text/markdown',
  url='https://github.com/AlonsoMartinToledano/pokedatabase_sdk',
  author='Alonso Martin-Toledano',
  author_email='alonsomtgm@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='pokemon, APIRest, SDK',
  packages=find_packages(),
  install_requires=['requests']
)