import setuptools

VERSION = '0.0.1'

setuptools.setup(
    name='stashboard',
    version=VERSION,
    description='Stash Horizon Dashboard',
    author='Rackspace',
    author_email='stash-devs@rackspace.com',
    packages=setuptools.find_packages(exclude=['test']),
    include_package_data=True,
    install_requires=[
        'python-troveclient',
    ],
    classifiers=[],
)
