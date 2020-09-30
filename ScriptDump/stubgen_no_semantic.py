import glob
import os
import shutil
import sys
import subprocess
import random


count1 = 0

path = "/home/bew/archive/typed_project/"
output_path = "/home/bew/Desktop/wp2/pyi/out/"
noSem_path = "/home/bew/Desktop/wp2/pyi/allrepo/Uninf_noImp_noSemantic/"
source_path = "/home/bew/Desktop/wp2/pyi/allrepo/source/"

os.chdir("/home/bew/Desktop/wp2/pyi/")

if 0:
	fpWrite = open("/home/bew/Desktop/wp2/pyi/allrepo/list.txt", 'w')
	for f in glob.glob("*.pyi"):
		count1 +=1
		#os.rename(f,str(count1) + "-Stripped.pyi")
		fpWrite.write("%s\n" % f)
	print(count1)

i = 0
with open("/home/bew/Desktop/wp2/pyi/allrepo/list.txt") as fpp:
	for ff in fpp:
		if os.path.isdir(output_path):
			shutil.rmtree(output_path)

		if i < -1:
			i += 1
			continue

		f = ff.strip()
		x = f.replace("*","/")
		x = x[:-1]
		print(i, x)
		i += 1
		subprocess.call(["stubgen", "--include-private", "--no-import", "--parse-only", path + x])
		#subprocess.call(["cp", path + x, source_path + str(i) + ".py"])
		j = 0
		for h in glob.glob(output_path +"*.pyi"):
			if j > 0:
				print("BUGGGGGGGGGGGGGGGGGGGGGGG")
			j += 1
			#print(h)
			name = str(i) + "-Uninf_noImp_noSemantic.pyi"
			os.rename(h,output_path + name)
			subprocess.call(["cp", output_path + name, noSem_path + name])

		#os.rename(ori_path + f, ori_path + str(i) + "-Original.pyi")
		#os.rename(str_path + f, str_path + str(i) + "-Stripped.pyi")


#with open("/home/bew/Desktop/wp2/pyi/allrepo/original") as ff:

