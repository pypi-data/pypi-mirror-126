# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['psfmachine']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=4.2,<5.0',
 'corner>=2.1.0,<3.0.0',
 'fitsio>=1.1.3,<2.0.0',
 'jedi==0.17.2',
 'lightkurve>=2.0.4,<3.0.0',
 'matplotlib>=3.3.3,<4.0.0',
 'numpy>=1.19.4,<2.0.0',
 'pandas>=1.1,<2.0',
 'patsy>=0.5.1,<0.6.0',
 'photutils>=1.1.0,<2.0.0',
 'pyia>=1.2,<2.0',
 'scipy>=1.5.4,<2.0.0',
 'tqdm>=4.54.0,<5.0.0']

setup_kwargs = {
    'name': 'psfmachine',
    'version': '1.1.0',
    'description': 'Tool to perform fast PSF photometry of primary and background targets from Kepler/K2 Target Pixel Files',
    'long_description': '# PSFMachine\n\n*PRF photometry with Kepler*\n\n<a href="https://github.com/ssdatalab/psfmachine/workflows/tests.yml"><img src="https://github.com/ssdatalab/psfmachine/workflows/pytest/badge.svg" alt="Test status"/></a>\n<a href="https://pypi.python.org/pypi/psfmachine"><img src="https://img.shields.io/pypi/v/psfmachine" alt="pypi status"></a>\n<a href="https://zenodo.org/record/4784073"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4784073.svg"></a>\n\nCheck out the [documentation](https://ssdatalab.github.io/psfmachine/).\nCheck out the [paper](#)\n\n`PSFMachine` is an open source Python tool for creating models of instrument effective Point Spread Functions (ePSFs), a.k.a Pixel Response Functions (PRFs). These models are then used to fit a scene in a stack of astronomical images. `PSFMachine` is able to quickly derive photometry from stacks of *Kepler* images and separate crowded sources.\n\n# Installation\n\n```\npip install psfmachine\n```\n\n# Example use\n\nBelow is an example script that shows how to use `PSFMachine`. Depending on the speed or your computer fitting this sort of model will probably take ~10 minutes to build 200 light curves. You can speed this up by changing some of the input parameters.\n\n```python\nimport psfmachine as psf\nimport lightkurve as lk\ntpfs = lk.search_targetpixelfile(\'Kepler-16\', mission=\'Kepler\', quarter=12, radius=1000, limit=200, cadence=\'long\').download_all(quality_bitmask=None)\nmachine = psf.TPFMachine.from_TPFs(tpfs, n_r_knots=10, n_phi_knots=12)\nmachine.fit_lightcurves()\n```\n\nFunding for this project is provided by NASA ROSES grant number 80NSSC20K0874.\n',
    'author': 'Christina Hedges',
    'author_email': 'christina.l.hedges@nasa.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://ssdatalab.github.io/psfmachine/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
