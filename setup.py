from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='heptasolver',
    version='0.1.0',
    description='Resuelve automáticamente el juego Heptagrama',
    author='narodr',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    include_package_data=True,
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'heptasolver=cli:cli',
        ],
    },
)
