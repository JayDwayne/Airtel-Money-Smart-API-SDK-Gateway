from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='airtel-python-sdk',
      version='0.1',
      description='Airtel Smart API SDK',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/sartim/airtel-python-sdk',
      author='sartim',
      license='MIT',
      packages=['airtel', ],
      install_requires=['requests', ],
      zip_safe=False
      )
