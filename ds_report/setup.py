from setuptools import setup

setup(name='ds_report',
      version='0.1',
      description='This is a prototype for report generating',
      url='https://github.com/datanooblol/ds_report.git',
      author='datanooblol',
      author_email='data.noob.lol@gmail.com',
      license='MIT',
      packages=['ds_report'],
      install_requires=[
          'numpy',
          'pandas'
          ],
      zip_safe=False)