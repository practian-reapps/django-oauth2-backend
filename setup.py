import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-oauth2-backend',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='oAuth2 with a Django backend',
    long_description=README,
    url='https://www.example.com/',
    author='Angel Sullon',
    author_email='asullom@gmail.com',
    classifiers=[
        'Environment :: API REST Environment',
        'Framework :: Django',
        'Framework :: DjangoREST Framework :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'docutils>=0.12',
        'Django>=1.10.*',
        'Pillow>=3.4.2',
        # 'django-cors-headers>=1.2.2',
        # 'djangorestframework>=3.5.2',
        # 'django-oauth-toolkit>=0.10.0',

    ],
)
