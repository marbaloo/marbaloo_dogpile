from setuptools import setup
readme = open('README.rst').read()

setup(name='marbaloo_dogpile',
      version='0.1.0',
      description='Dogpile support for cherrypy.',
      long_description=readme,
      url='http://github.com/marbaloo/marbaloo_dogpile',
      author='Mahdi Ghane.g',
      license='MIT',
      keywords='dogpile cherrypy marbaloo marbaloo_dogpile',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Framework :: CherryPy',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Software Development :: Libraries'
      ],
      install_requires=[
          'cherrypy>=8.1.2',
          'dogpile.cache>=0.6.2'
      ],
      packages=['marbaloo_dogpile'],
      )



