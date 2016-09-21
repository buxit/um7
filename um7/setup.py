from setuptools import setup

setup(name='UM7',
      version='0.9',
      description='Classes to interface with CH Robotics UM7 IMU',
      url='https://pypi.python.org/pypi/um7/0.9',
      author='Daniel Kurek',
      author_email='dkurek93@gmail.com',
      license='MIT',
      packages=['UM7'],
      install_requires=['pyserial', 'numpy'],
      zip_safe=False)
