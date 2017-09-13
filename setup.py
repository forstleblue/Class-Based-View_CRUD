from setuptools import find_packages, setup

setup(
    name='booksapp',
    version='0.1.1',
    author='Constverum',
    author_email='constverum@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'wheel==0.29.0',
        'django==1.10.5',
        'nose==1.3.7',
        'django-nose==1.4.4',
        'nosedjango==1.0.13',
    ],
    test_suite='tests',
    tests_require=['nose'],
)
