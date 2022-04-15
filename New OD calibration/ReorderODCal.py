import json
from sys import argv
import os

if len(argv) != 3:
    print('Usage: python ReorderODCal.py /path/to/calibrations.json od_cal_name')
    exit()


cal_file = argv[1]
if not os.path.isfile(cal_file):
    print(f"Calibration file not found.")
    exit()

cal_dir = os.path.dirname(cal_file)
cal_name = argv[2]

j = json.load(open(cal_file, 'r'))

names = []  # Store valid OD names
for c, cal in enumerate(j):  # Iterate over calibrations list
    if cal["calibrationType"] == "od":
        names.append(cal["name"])

        if cal["name"] == cal_name:
            originalOD = cal["measuredData"][0]

            # Create new 'measuredData' list of ODs
            lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            new_order = []
            for v in range(16):
                # Create lists that show the order in which each vial measures the OD cultures (index list)
                v_list = lista[15+v+1 : v : -1]

                # Take the OD value measured in each go and, for each vial,
                # place it in the position of the OD that eVOLVER think it's measuring

                new_list = [None]*16
                for i, value in enumerate(v_list):
                    new_list[v_list[i]] = originalOD[i]  # Substitute index by OD value

                new_order.append(new_list)

            # Update "measuredData" in original data
            j[c]["measuredData"] = new_order
            break
else:
    print(f'Calibration "{cal_name}" not found. These are the available OD calibrations')
    print(names)
    exit()


json.dump(j, open(os.path.join(cal_dir, 'calibrations.json.out'), 'w'))
print(f'Calibration "{cal_name}" correctly updated')
