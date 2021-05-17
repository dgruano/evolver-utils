#evolver-utils
This is a set of Python scripts we use in the SyntheCell
team to analyse data and interact with the eVOLVER. I coded
everything using a Mac, so there may be some parts not
optimised for Windows.


## Delete calibrations
Using `deleteCal.py` you can clean the calibration list
of your eVOLVER.

```shell script
# Download calibration file
scp pi@<evolver_ip>:evolver/evolver/calibrations.json calibrations.json

# List available calibrations
python deleteCal.py calibrations.json -l

# Delete calibration
python deleteCal.py calibrations.json -n <cal_name>

# Upload new calibration file
scp ./calibrations.json pi@<evolver_ip>:evolver/evolver/calibrations.json
```