import io
import os
from pathlib import Path
from setuptools import find_packages, setup

NAME = 'pred_model'
DESCRIPTION = 'Network Congestion Prediction Model'
URL = 'https://github.com/prpa4901/network-congestion-mlops'
EMAIL = 'priteshlp243@gmail.com'
AUTHOR = 'Pritesh Patil'
REQUIRES_PYTHON = '>=3.10.11'

pwd = os.path.abspath(os.path.dirname(__file__))

def list_reqs(fname='requirements.txt'):
    with io.open(os.path.join(pwd, fname), encoding='utf-8') as f:
        return f.read().splitlines()

try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

ROOT_PACKAGE = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_PACKAGE/NAME
about = {}

with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'pred_model': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
)


