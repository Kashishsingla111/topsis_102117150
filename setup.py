from distutils.core import setup
setup(
  name = 'topsis-Kashish-102117150',         # How you named your package folder (MyLib)
  packages = ['topsis-Kashish-102117150'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This Python package implements the Topsis (Technique for Order Preference by Similarity to Ideal Solution) algorithm. Topsis is a multi-criteria decision-making (MCDM) method that helps in choosing the best alternative from a set of alternatives based on their performance on multiple criteria.',   # Give a short description about your library
  author = 'Kashish',                   # Type in your name
  author_email = 'kkashish_be21@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/Kashishsingla111/topsis_102117150',   # Provide either the link to your github or to your website
  keywords = ['PYTHON', 'TOPSIS', 'MCDM'],   # Keywords that define your package best
  classifiers=[      
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)