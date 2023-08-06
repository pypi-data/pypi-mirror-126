# coding: utf-8
# python setup.py sdist register upload
import re
from os.path import join, dirname

from setuptools import setup

_init_py = join(dirname(__file__), '__init__.py')
_requirements_txt = join(dirname(__file__), 'requirements.txt')


def increment_ver(version):
    version = version.split('.')
    version[2] = str(int(version[2]) + 1)
    return '.'.join(version)


with open(_init_py) as fp:
    for line in fp:
        m = re.search(r'^\s*__version__\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
        if m:
            before_version = m.group(2)
            new_version = increment_ver(before_version)
            break
    else:
        raise RuntimeError('Unable to find own __version__ string')

with open(_init_py, mode='r') as f:
    _before_version = f"__version__ = '{before_version}'"
    _new_version = f"__version__ = '{new_version}'"
    _src = f.read().replace(_before_version, _new_version)

with open(_init_py, mode='w') as f:
    f.write(_src)

_requirements = []
with open(_requirements_txt, mode='r') as f:
    __requirements = f.readlines()
    for _ in __requirements:
        c = _[0].strip()
        if _[0] == "#" or _[0] == "\n":
            continue
        _ = _.replace("\n", "")
        _requirements.append(f'{_}')

setup(
    name='bvx-es',
    version=new_version,
    description='elasticsearch util singleton class.',
    author='Kazuhiro Kotsutsumi',
    url='https://github.com/kotsutsumi/bvx-es',
    packages=['bvx_es'],
    include_package_data=True,
    license='The MIT License',
    install_requires=_requirements,
)

# EOF
