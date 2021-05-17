import json
import os
import argparse

# Deal with input arguments
parser = argparse.ArgumentParser(
    epilog="And remember to first download your calibrations file from eVOLVER...")
parser.add_argument("file", help="path to the calibrations file")
parser.add_argument("-n", "--name", help="name of the calibration to be deleted", dest='name', action='store')
parser.add_argument("-l", "--list", help="list available calibrations",
                    action="store_true")
parser.add_argument("-y", help="answer yes to all the script prompts",
                    action="store_true")
args = parser.parse_args()

cal_file = args.file
if not os.path.isfile(cal_file):
    print(f"Calibration file not found.")
    exit()

cal_dir = os.path.dirname(cal_file)
cal_name = args.name

# TOD: Connect to eVOLVER to get calibrations.json file

# Load calibrations.json
j = json.load(open(cal_file, 'r'))

# Store calibration names by type
od_cals = []
temp_cals = []
found = False
for c, cal in enumerate(j):  # Iterate over calibrations list
    cal_type = cal["calibrationType"]
    if cal_type == "od":
        od_cals.append(cal["name"])

    elif cal_type == "temperature":
        temp_cals.append(cal["name"])

    if cal["name"] == cal_name:
        found = True
        print(f'{cal_type} calibration "{cal_name}" found.')
        if args.y or input("Delete? (y/n)") == "y":
            # Delete and save remaining calibrations to file
            del j[c]
            json.dump(j, open(os.path.join(cal_dir, 'calibrations.json'), 'w'))
            print("Deleted.")

if args.list or not found:
    print('These are the available calibrations:')
    print()
    print('*Temp Cals*')
    print('\n'.join(temp_cals))
    print()
    print('*OD Cals*')
    print('\n'.join(od_cals))

if cal_name and not found:
    print()
    print(f"Calibration {cal_name} not found.")
    print("See available calibrations above")



