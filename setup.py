from setuptools import setup


setup(
    name='smartchoices',
    version='1.0',
    description='A smart choices interface for Django apps',
    long_description=open('README.md', 'r').read(),
    author='Storybird Developers',
    author_email='dev@storybird.com',
    url='https://github.com/storybird/smartchoices',
    license='MIT',
    packages=('smartchoices',),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
