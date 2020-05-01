import os
import shutil
import sys
import subprocess
import random

path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
path_repo = "/home/bew/archive/typed_project/"
path_ori = "/home/bew/Desktop/wp2/pyi/original/"
path_str = "/home/bew/Desktop/wp2/pyi/stripped/"
path_pyi = "/home/bew/Desktop/wp2/pyi/.pytype/pyi/"
path_output_ori = "/home/bew/Desktop/wp2/pyi/allrepo/original/"
path_output_str = "/home/bew/Desktop/wp2/pyi/allrepo/stripped/"
write_path = "/home/bew/Desktop/wp2/pyi/error"
LIM = 3

os.chdir("/home/bew/Desktop/wp2/pyi")
shutil.rmtree(path_ori)
shutil.rmtree(path_str)
os.mkdir(path_ori)
os.mkdir(path_str)

random.seed(version = 2)
iii = 0
fpWrite = open(write_path, 'w')
for ii in range(1,28):
	if ii  == 25:
		continue
	path_repo_list_num = path_repo_list + str(ii)
	#write_path_num = write_path + str(ii)
	#fpWrite = open(write_path_num, 'w')
	with open(path_repo_list_num) as fp:
		line = fp.readline()
		while line:
			repo_name = line.strip()

			subprocess.call(["cp","-r",path_repo + repo_name,path_ori])
			num_file = 0
			for root, dirs, files in os.walk(path_ori + repo_name):
				y = root
				y = y.replace("/original/","/stripped/")
				os.mkdir(y)
				for file in files:
					if file.endswith(".py"):
						num_file += 1
						x = f"{os.path.join(root, file)}"
						x = x.replace("/original/","/stripped/")
						subprocess.call(["./strip.sh", f"{os.path.join(root, file)}", x])

			a = []
			print(num_file)
			if num_file >= LIM:
				a = random.sample(range(0,num_file), LIM)
			else:
				a = [0,1,2,3,4]
			print(a)

			i = 0
			samples = []
			for root, dirs, files in os.walk(path_ori + repo_name):
				for file in files:
					if file.endswith(".py"):
						if i in a:
							x = f"{os.path.join(root, file)}"
							samples.append(x)

						i += 1						
			print(samples)
			
			for s in samples:
				ss = s.replace("/original/","/stripped/")
				print("-------------------------------------------------------")
				print(s)
				print(ss)
				f_s = s.replace(path_ori,"")
				#f_ss = ss.replace(path_str,"")
				f_s = f_s.replace("/","--") + "i"
				#f_ss = f_ss.replace("/","--") + "i"
				print(f_s)
				#print(f_ss)
				E = s.split("/")
				
				shutil.rmtree(path_pyi)
				os.mkdir(path_pyi)
				command = ["pytype","-k","-d","import-error"]
				command.append(s)
				temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
				output,o2 = temp.communicate()
				output = str(output.decode('ascii','ignore'))
				o2 = str(o2.decode('ascii','ignore'))
				print("{} {} output = {}".format(ii,iii,output))

				found = 0
				x = ""
				y = ""
				for root, dirs, files in os.walk(path_pyi):
					if found == 1:
						break
					for file in files:
						if file.endswith(".pyi"):
							if file == E[-1] + "i":
								found = 1
								x = f"{os.path.join(root, file)}"
								y = f"{os.path.join(root, f_s)}"
								break
				if found == 0:
					print("BUGGGGGGGGGGGGGGGGGGGGG")
					fpWrite.write("%s\n" % x)
					continue
					#sys.exit()

				#print("x = " + x)
				#print("y = " + y)
				os.rename(x,y)
				subprocess.call(["cp",y,path_output_ori])


				shutil.rmtree(path_pyi)
				os.mkdir(path_pyi)
				command = ["pytype","-k","-d","import-error"]
				command.append(ss)
				temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
				output,o2 = temp.communicate()
				output = str(output.decode('ascii','ignore'))
				o2 = str(o2.decode('ascii','ignore'))
				print("{} {} output = {}".format(ii,iii,output))

				found = 0
				x = ""
				y = ""
				for root, dirs, files in os.walk(path_pyi):
					if found == 1:
						break
					for file in files:
						if file.endswith(".pyi"):
							if file == E[-1] + "i":
								found = 1
								x = f"{os.path.join(root, file)}"
								y = f"{os.path.join(root, f_s)}"
								break
				if found == 0:
					print("BUGGGGGGGGGGGGGGGGGGGGG_2")
					fpWrite.write("%s\n" % x)
					continue
					#sys.exit()

				#print("x = " + x)
				#print("y = " + y)
				os.rename(x,y)
				subprocess.call(["cp",y,path_output_str])




			#break;
			line = fp.readline()
			iii += 1
	fp.close()
fpWrite.close()