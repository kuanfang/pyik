from setuptools import setup, find_packages
import sys

setup(name='pyik',
      packages=[package for package in find_packages()
                if package.startswith('pyik')],
      install_requires=['sympy', 'scipy'],
      description="Python package for inverse kinematics.",
      author="Kuan Fang",
      url='https://github.com/kuanfang/pyik',
      author_email="dont_contact_me@noneofyourbusiness.com",
      version="1.0")
