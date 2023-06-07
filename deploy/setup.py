from setuptools import setup, find_packages

setup(
    name='recommendation system',
    version='1.0',
    # scripts=['app.py'],
    packages=find_packages(),
    install_requires=[
          'flask',
          'flask_expects_json',
          'python-dotenv',

      ],
)
