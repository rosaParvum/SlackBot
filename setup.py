from setuptools import setup

setup(name='slackbottools',
      version='2.0',
      description='A python package built for writing SlackBots',
      url='https://github.com/coderplans/SlackBot',
      author='coderplans',
      author_email='thomas@khandaan.org',
      license='Apache 2.0',
      packages=['slackbottools'],
      install_requires =[
          'slackclient'
          ],
      zip_safe=False)
