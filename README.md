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


