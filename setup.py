import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-simple-math-captcha',
    version='0.1.0',
    packages=['wagtail-simple-math-captcha'],
    install_requires=['django-simple-math-captcha'],
    include_package_data=True,
    license='BSD License',
    description='A simple math captcha field for Wagtail Form Pages based on Django Simple Math Captcha.',
    long_description=README,
    url='https://bitbucket.org/jordanmarkov/wagtail-simple-math-captcha',
    author='Jordan Markov',
    author_email='jmarkov@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
