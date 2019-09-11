from setuptools import find_packages
from setuptools import setup

auth = ''
bitbucket_repo = 'git+https://%sbitbucket.org/naimuri/' % auth

naimuri_dependencies = {
    'cyrm_common': 'cyrm_common',
    'cyrm_python_tools_framework': 'cyrm_python_tools_framework'
}
naimuri_dependency_links = [bitbucket_repo + repo + '/master#egg=' + egg
                            for repo, egg in naimuri_dependencies.iteritems()]

setup(
    name="python_sns",
    version='0.1.DEVELOPMENT_BUILD',
    description='Sends an SNS message to an AWS SNS topic defined by en env var',
    author='Naimuri',
    packages=find_packages(),
    install_requires=['nose',
                      'coverage',
                      'boto3'] + naimuri_dependencies.values(),
    dependency_links=naimuri_dependency_links
)
