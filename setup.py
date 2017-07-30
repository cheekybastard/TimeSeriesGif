from distutils.core import setup
setup(
  name = 'TimeSeriesGif',
  packages = ['TimeSeriesGif'],
  version = '0.1',
  description = 'Create gifs from pandas time series.',
  author = 'Andrew Han',
  author_email = '',
  url = 'https://github.com/handrew/TimeSeriesGif', 
  download_url = '', 
  keywords = ['time series', 'pandas', 'visualization'], 
  classifiers = [],
  install_requires=[
      "matplotlib",
      "imageio",
      "pandas",
      "numpy",
  ],
)