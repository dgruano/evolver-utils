## `ReorderODCal.py`

This script reorganises the OD data of a calibration when running the new calibration protocol (fixed vials with subsequent cell inoculation) while using the original calibration software (rotation of 16 vials with different concentrations of cells).

### Usage

First, make a new folder and `cd` into it. Then, connect to eVOLVER and download the `calibrations.json` using `scp`.

```
## (In eVOLVER Computer) ##
# Download the file from the eVOLVER
scp pi@<evolver IP>:evolver/evolver/calibrations.json calibrations.json

# Then run:
python ReorderODCal.py </path/to/calibrations.json> <od_cal_name>
```

- `/path/to/calibrations.json`: path where your calibration files is
- `od_cal_name`: name you gave to your calibration

The script will output a new updated calibrations file (`calibrations.json.out`) in the same folder as the original.

Finally, upload the updated file to the eVOLVER using `scp`:

```
# Upload the file to eVOLVER
scp </path/to/calibrations.json.out> pi@<evolver IP>:evolver/evolver/calibrations.json
```

## `BackCalculatedODCal.py`

This script works exactly as `ReorderODCal.py`, except that you have to input the list with the 16 different ODs that were measured during the calibration. This way, if you measured the OD of the vials at the end of the calibration, you can "back-calculate" the 16 OD points that eVOLVER measured during the calibration. We have seen this approach is more accurate.

### Usage

First, make a new folder and `cd` into it. Then, connect to eVOLVER and download the `calibrations.json` using `scp`.

```
## (In eVOLVER Computer) ##
# Download the file from the eVOLVER
scp pi@<evolver IP>:evolver/evolver/calibrations.json calibrations.json
```

Before running the script, open it and edit the list `originalOD = [...]` filling it with the back-calculated ODs.

Then run:
```
python BackCalculatedODCal.py </path/to/calibrations.json> <od_cal_name>
```

- `/path/to/calibrations.json`: path where your calibration files is
- `od_cal_name`: name you gave to your calibration

The script will output a new updated calibrations file (`calibrations.json.out`) in the same folder as the original.

Finally, upload the updated file to the eVOLVER using `scp`.

```
# Upload the file to eVOLVER
scp </path/to/calibrations.json.out> pi@<evolver IP>:evolver/evolver/calibrations.json
```

### Download and upload calibration files from eVOLVER

```
## (In eVOLVER Computer) ##
# Download the file from the eVOLVER
scp pi@<evolver IP>:evolver/evolver/calibrations.json calibrations.json


# Upload the file to eVOLVER
scp </path/to/calibrations.json.out> pi@<evolver IP>:evolver/evolver/calibrations.json
```