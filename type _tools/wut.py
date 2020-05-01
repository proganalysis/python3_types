import subprocess
import os
import shutil
import glob
from operator import itemgetter


print("Hi")
count = 0
total_file = 0
rem_file = 0
rem_filtered = 0
xx = []
dd = dict()

with open("/home/bew/Desktop/wp2/FilteredRepoNFiles/notMypy") as ff:
	for f in ff:
		x = f.strip()
		dd[x] = 1
with open("/home/bew/Desktop/wp2/FilteredRepoNFiles/Stats") as fp:
	for f in fp:
		x = f.strip().split(' ')
		count += 1
		rem_file += int(x[0])
		total_file += int(x[1])
		y = [int(x[0]), int(x[1]), float(x[2]), x[3]]
		if x[3] in dd:
			y.append("X")
		else:
			y.append("O")
			rem_filtered += int(x[0])
		xx.append(y)

xx.sort(key=itemgetter(1,0), reverse = True)


print("Total repo = {}".format(count))
print("Total files = {}".format(total_file))
print("After filtered = {}".format(rem_file))
print("{}".format(rem_filtered))

jj = 0
for y in xx:
	jj += 1
	if jj < 200:
		g = "%4d" % y[0]
		h = "%4d" % y[1]
		f = "%.6f" % y[2]
		print("{}\t{}\t{}\t{}\t{}".format(g,h,f,y[4],y[3]))
		#print(y)

if 0:
	path_file_list = "/home/bew/Desktop/wp2/FilteredRepoNFiles/Files/"
	repo = "(yokawasa)azure-functions-python-samples"

	os.chdir("/home/bew/archive/typed_project")

	full_repo_path = "/home/bew/archive/typed_project/(lupoDharkael)flameshot"

	#all_files = glob.glob(full_repo_path + "/**/*.py", recursive = True)
	command = ["mypy"]
	command.append("--show-error-codes")
	command.append("--namespace-packages")
	command.append("--ignore-missing-imports")
	command.append("--show-column-numbers")

	with open(path_file_list + repo + ".txt") as fp:
		for f in fp:
			x = f.strip()
			print(x)
			command.append(x)

	temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
	output,o2 = temp.communicate()
	output = str(output.decode('ascii','ignore'))
	o2 = str(o2.decode('ascii','ignore'))
	print("1 = {}".format(output))
	print("2 = {}".format(o2))



if 0:
	all_files = []
	for r,d,f in os.walk(full_repo_path):
		for file in f:
			if '.py' in file:
				if '.pyc' not in file:
					all_files.append(os.path.join(r,file))


if 0:
	queue = [full_repo_path]
	all_files = []
	while 1:
		print(queue)
		if len(queue) == 0:
			break
		x = queue[0]
		del queue[0]
		if x.lower().endswith('.py'):
			all_files.append(x)
		elif os.path.isdir(x):
			y = os.listdir(x)
			queue = queue + y

	all2 = []
	with open("/home/bew/Desktop/wp2/FilteredRepoNFiles/Files/(kalaspuff)tomodachi.txt") as fp:
		for f in fp:
			g = f.strip()
			all2.append(g)
	for f in all_files:
		if f not in all2:
			print(f) 
		#print(f)
	#print(all_files) 
	print(len(all2))
	print(len(all_files))