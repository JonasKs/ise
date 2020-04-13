from setuptools import find_packages, setup


setup(
    name='ISE',
    version='1.1.0',
    py_modules=['ise'],
    url='',
    license='LICENSE.md',
    maintainer='Andreas Falk',
    maintainer_email='falk@sadsloth.net',
    description='',
    long_description='README.md',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'furl>=1.2.1',
        'requests>=2.18.4'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage'
        ],
    },
)
