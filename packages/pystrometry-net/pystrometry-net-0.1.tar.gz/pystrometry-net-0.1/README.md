# Pystrometry.net
Python interface for a local installation of the astrometry.net plate solver.

## Purpose
The purpose of this project is to expose the functionality of local plate solving via Astrometry.net to Python for use in data reduction pipelines and the like.

## Installation
Pystrometry.net requires a local installation of Astrometry.net with appropriate index files. Astrometry must be in PATH!

## Usage
Pystrometry.net contains a wrapper for the solve-field command from astrometry.
```
from astropy.io import fits
from pystrometry import solve

hdul = fits.open('test-data/60.0s-B-fut_2021-09-28T22-11-04.fits.gz')

RA, DEC = hdul[0].header['OBJ-RA']/24 * 360, hdul[0].header['OBJ-DEC']
solvedheader = solve.solveField(hdul,RA,DEC)
```
