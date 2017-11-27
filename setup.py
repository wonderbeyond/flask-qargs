from setuptools import setup, find_packages


setup(
    name='Flask-QArgs',
    version='0.0.2',
    description='Flask Query Arguments Parser, as your view decorators.',
    author='Wonder',
    author_email='wonderbeyond@gmail.com',
    url='https://www.github.com/wonderbeyond/flask-qargs',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'Flask-RESTful~=0.3.6',
    ],
)
