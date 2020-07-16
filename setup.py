import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='nbmerge',
    version='0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/stacks13/nbmerge',
    license='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sahil Nirkhe',
    author_email='sahilnirkhe@outlook.com',
    description='Merges multiple notebooks together',
    python_requires='>=3.6',
)
