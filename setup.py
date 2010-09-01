from distutils.core import setup

setup(name='django-venues',
      version="0.1",
      description='Venues for django',
      long_description="Venues for django",
      author='Philipp Wassibauer',
      author_email='phil@maptales.com',
      url='http://github.com/philippWassibauer/django-venues',
      packages=['venues','venues.templatetags'],
      package_data={'actstream':['venues/templates/venues/*.html']},
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
