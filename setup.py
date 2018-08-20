from setuptools import setup

REQUIREMENTS = [
    'requests',
    'click'
]

VERSION = 0.5
REPO_URL = 'https://github.com/BoxingOctopus/toxin'

setup(
    name='toxin',
    packages=['toxin'],
    scripts=['toxin/toxin'],
    version=VERSION,
    description='An LFI (Local File Inclusion) Exploitation Tool',
    author='Ryan Draga',
    author_email='ryan.draga@boxingoctop.us',
    url=REPO_URL,
    download_url='{0}/archive/{1}.tar.gz'.format(REPO_URL, str(VERSION)),
    keywords=['LFI', 'Exploit'],
    python_requires='>=3.0',
    install_requires=REQUIREMENTS,
    classifiers=[]
)
