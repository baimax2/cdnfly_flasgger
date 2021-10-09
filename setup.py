from setuptools import setup, find_packages

setup(
    name='flasgger',
    version='0.4.3',
    url='https://github.com/baimax2/cdnfly_flasgger',
    license='MIT',
    author='Baimax',
    author_email='baimax@funnull.com',
    description='Extract swagger specs from cdnfly flask project',
    packages=["flasgger"]
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'PyYAML>=3.0',
        'jsonschema>=3.0.1',
        'mistune',
        'six>=1.10.0'
    ]
)
