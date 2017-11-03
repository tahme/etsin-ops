from setuptools import setup

setup(
    name='etsin_search_index',
    packages=['etsin_search_index'],
    include_package_data=True,
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ]
)
