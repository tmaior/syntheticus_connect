from setuptools import setup, find_packages

setup(
    name='syntheticus_connect',
    version='0.1.6',
    description='A Python client for Syntheticus',
    author='Valerio Mazzone',
    author_email='valerio.mazzone@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'tabulate',
        'ipywidgets',
        'ipython'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
