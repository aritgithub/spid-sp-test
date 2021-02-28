from glob import glob
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

_src_folder = 'src'
_pkg_name = 'spid_sp_test'

setup(
    name='spid_sp_test',
    version='0.2.6',
    description="SAML2 SPID Service Provider validation tool that can be run from the command line",
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
                 'Programming Language :: Python :: 3'],
    url='https://github.com/peppelinux/spid-sp-test',
    author='Giuseppe De Marco',
    author_email='giuseppe.demarco@tamdigitale.governo.it',
    license='BSD',
    scripts=['src/spid_sp_test/spid_sp_test'],
    packages=[f"{_pkg_name}"],
    package_dir={f"{_pkg_name}": f"{_src_folder}/spid_sp_test"},
    
    package_data={f"{_pkg_name}": [i.replace(f'{_src_folder}/{_pkg_name}/', '') 
                                   for i in glob(f'{_src_folder}/{_pkg_name}/**', 
                                                 recursive=True)]
    },
    install_requires=[
                'lxml',
                'pysaml2',
                'xmlschema',
                'requests',
                'pyXMLSecurity'
              ],
    )
    