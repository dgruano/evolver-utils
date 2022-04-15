from sys import argv
import os

if len(argv) == 1:
	print("Assuming OD data is in local directory")
	path = "."
elif len(argv) == 2:
	path = argv[1]
	print(f'Analyzing dir: {path}')


data = {}

for i in range(0,16):

	filename = os.path.join(path, 'vial%d_OD.txt'%i)
	F = open(filename)
	timepoints = []
	ods = []
	for line in F:
		if line.startswith('E'):
			continue
		line = line.strip('\n').split(',')
		h = line[0]
		od = line[1]

		timepoints.append(float(h))
		ods.append(float(od))

	data[i] = [timepoints, ods]


while True:
	vial = input("Insert vial number: ")
	time = input("Insert time (h): ")
	#time = 2.3
	print()

	if vial == 'end' or time == 'end':
		print('Exiting...')
		exit()

	try:
		time = float(time)
	except ValueError:
		print("Time should be a number")
		print('Exiting...')
		exit()

	try:
		vial = int(vial)
	except ValueError:
		print("Vial number should be a number")
		print('Exiting...')
		exit()

	if vial not in range(-1,16):
		print("Vial number out of range")
		print('Exiting...')
		exit()

	print('OD for time %.2f h: '%time)
	print()

	if vial == -1:
		for vial in range(0,16):
			timepoints = data[vial][0]
			ods = data[vial][1]
			for x in range(len(timepoints)):
				if timepoints[x] >= time:
					mean = sum(ods[x-4:x+6])/10
					# print('Vial %d\t%.3f'%(vial, ods[x]))
					#print('Vial %d\t%.3f'%(vial, mean))
					print('%.3f'%mean)
					break
	else:
		timepoints = data[vial][0]
		ods = data[vial][1]
		for x in range(len(timepoints)):
			if timepoints[x] >= time:
				mean = sum(ods[x-2:x+3])/5
				# print('Vial %d\t%.3f'%(vial, ods[x]))
				print('Vial %d\t%.3f'%(vial, mean))
				break

	print()


