from distutils.core import setup
setup(
  name = 'libFLIR',
  packages = ['libFLIR'],
  version = '1.4',
  description = 'FLIR TAU Control Library',
  author = 'Weqaar Janjua',
  author_email = 'weqaar.janjua@gmail.com',
  url = 'https://github.com/weqaar/libflir',
  download_url = 'https://github.com/weqaar/libflir/tarball/0.1',
  keywords = ['libflir', 'thermal', 'flir'],
  classifiers = [],
  install_requires=[
      "pyserial >= 3.2.1",
      "crc16 >= 0.1.1",
  ],
)
