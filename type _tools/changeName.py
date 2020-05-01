import subprocess
import os
import shutil
import glob

read_path = "/home/bew/Desktop/wp2/pyi/allrepo/"

all_files = glob.glob(read_path + "original" + "/**/*.pyi", recursive = True)
i = 0
for f in all_files:
	if "jpn--" in f:
		continue
	if "rahiel" in f:
		continue
	x = f.replace("--","*")
	os.rename(f,x)

all_files_2 = glob.glob(read_path + "stripped" + "/**/*.pyi", recursive = True)
j = 0

for f in all_files_2:
	if "jpn--" in f:
		continue
	if "rahiel" in f:
		continue
	x = f.replace("--","*")
	os.rename(f,x)


i = 0
for f in all_files:
	x = f.replace("*","/")
	x = x.replace("Desktop/wp2/pyi/allrepo/original/", "archive/typed_project/")
	x = x.replace(".pyi",".py")
	if not os.path.isfile(x):
		print(f)
		i += 1

all_files_2 = glob.glob(read_path + "stripped" + "/**/*.pyi", recursive = True)
j = 0

for f in all_files_2:
	x = f.replace("*","/")
	x = x.replace("Desktop/wp2/pyi/allrepo/stripped/", "archive/typed_project/")
	x = x.replace(".pyi",".py")
	if not os.path.isfile(x):
		print(f)
		j += 1
print(i)
print(j)
