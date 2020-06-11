## Introduction ##

This repository contains a notebook that will perform the following steps

* loading all data from a given folder + timepulse file (for the timing of the iamges)
* select OB folder (for normalization)
* select ROI in sample
* select instrument configuration
* select powder element to compare with measure Bragg Edges
* plot profile vs lambda
* export profile vs lambda into ascii file

## Instructions ##

To recover notebook, runs following commands

```
 $ python before_and_after_github_script.py -b
```

and before pushing to repository

```  
$ python before_and_after_github_script.py -a
```

## Requirements ##

tested with python 3.6

$ pip install plotly
$ pip install pillow
$ pip install pyqt=4.11.4
$ pip install NeuNorm
$ pip install neutronbraggedge
$ pip install nbstripout

$ conda install numpy
$ conda install jupyter 
$ conda install matplotlib
$ conda install -c neutrons ipywe
