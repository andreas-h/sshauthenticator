from setuptools import setup

setup(
    name='jupyterhub-sshauthenticator',
    version='0.1',
    description='SSH Authenticator for JupyterHub',
    url='https://github.com/andreas-h/sshauthenticator',
    author='Andreas Hilboll',
    author_email='hilboll@uni-bremen.de',
    license='3 Clause BSD',
    packages=['sshauthenticator'],
    install_requires=[
        'paramiko',
    ]
)
