import re
from os import path

from setuptools import setup, find_packages

version_file = path.join(
    path.dirname(__file__),
    'line_notify',
    '__version__.py'
)
with open(version_file, 'r') as fp:
    m = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        fp.read(),
        re.M
    )
    version = m.groups(1)[0]

setup(
    name='line-notify',
    version='0.0.1',
    url='git@ssh.dev.azure.com/v3/hyenatek/IOT/Cloud_Common.git',
    author='NiJia Lin',
    author_email='louis70109@gmail.com',
    license='MIT',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'dynaconf==2.2.2',
    ],
    zip_safe=False
)
