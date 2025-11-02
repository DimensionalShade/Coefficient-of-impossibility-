from setuptools import setup

setup(
    name='coefficient_of_impossibility',
    version='0.1.0',
    py_modules=['constants', 'xi'],
    entry_points={
        'console_scripts': [
            'xi = xi:main',
        ],
    },
)
