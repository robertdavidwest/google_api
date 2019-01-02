from setuptools import setup
from google_api import __version__
setup(name='google_api_rdw',
      version=__version__,
      description='Connect to the google api',
      url='https://github.com/robertdavidwest/google_api',
      author='Robert West',
      author_email='robert.david.west@gmail.com',
      license='MIT',
      packages=['google_api'],
      zip_safe=False)

