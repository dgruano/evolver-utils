# evolver-utils

This is a set of Python scripts and other resources we use in the SyntheCell
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

## Change LED Power

Using `changeLEDPower.py` you can modify the eVOLVER configuration
with the desired, individual LED powers.

You can give the script a single power (to update the 16 smart-sleeves)
with the same one:
```shell
python changeLEDPower.py -a 192.168.1.2 -p 2060 
```

or, alternatively, you can specify the power for every single sleeve (total of 16):
```shell
python changeLEDPower.py -a 192.168.1.2 -p 2060 2060 2060 2060 2062 2062 2062 2062 2064 2064 2064 2064
2068 2068 2068 2068
```
Run `python changeLEDPower.py -h` for additional info.

**Important:** You may want to backup the original configuration file
before using this script, in case something goes wrong. You can do it like this:

```shell
# Log in to your eVOLVER machine using ssh:
ssh pi@<evolver_ip>

# Backup your configuration file, just in case:
cp evolver/evolver/conf.yml evolver/evolver/conf.yml.bak
```

## Get OD at any given point
Simply run 
```
python get_od.py </path/to/experiment_expt/OD>
```

This is a loop script that reads the OD data from an experiment and lets you query for a specific vial and experiment time (in hours), and it will return the 10-value OD average around that time.  If you want the OD of all vials for a specified time, input -1 as the vial number.


## Calculate eVOLVER consumption

You can use the Excel sheet `eVOLVER Consumption.xlsx` to calculate the amount of medium you need for your experiment.
