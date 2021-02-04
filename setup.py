from setuptools import setup, find_packages

version="0.0.0"

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'pytest',
    'pytest-cov',
    'pytest-mock'
]

setup(
    name='skeleton',
    version=version,
    description=(
        'A bare bones Python package.'
    ),
    long_description=readme,
    long_description_content_type='text/markdown',

    author='Alex Nguyen',
    author_email='alex991nguyen@gmail.com',

    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires='>=3.6',
    install_requires=requirements,
    license='Apache License 2.0',
    keywords=[
        "skeleton",
        "python",
    ],
)
