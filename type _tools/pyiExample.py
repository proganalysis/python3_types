import os
import shutil
import subprocess

read_path = "/home/bew/Desktop/wp2/Info"
path_ori = "/home/bew/Desktop/wp2/pyi/original/"
path_str = "/home/bew/Desktop/wp2/pyi/stripped/"
path_repo = "/home/bew/archive/typed_project/"
path_pyi = "/home/bew/Desktop/wp2/pyi/.pytype/pyi/"
path_output = "/home/bew/Desktop/wp2/pyi/output/"

print(os.getcwd())
os.chdir("/home/bew/Desktop/wp2/pyi")
print(os.getcwd())
shutil.rmtree(path_ori)
shutil.rmtree(path_str)
os.mkdir(path_ori)
os.mkdir(path_str)

with open(read_path) as fp:
	line = fp.readline()
	while line:
		line = line.strip()
		# print(line)
		S = line.split(' ')
		print(S[1])
		E = S[1].split('/')
		print(E[0])

		subprocess.call(["cp","-r",path_repo + E[0],path_ori])

		for root, dirs, files in os.walk(path_ori + E[0]):
			y = root
			y = y.replace("/original/","/stripped/")
			os.mkdir(y)
			for file in files:
				if file.endswith(".py"):
					x = f"{os.path.join(root, file)}"
				    #print(root)
					x = x.replace("/original/","/stripped/")
					# print(x)
					subprocess.call(["./strip.sh", f"{os.path.join(root, file)}", x])

		command = ["pytype"]
		command.append("-k")
		command.append("-d")
		command.append("import-error")
		command.append(path_ori + S[1])
		temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
		output,o2 = temp.communicate()
		output = str(output.decode('ascii','ignore'))
		o2 = str(o2.decode('ascii','ignore'))
		print("output = {}".format(output))
		x = path_pyi + E[-1] + "i"
		y = path_pyi + S[0] + "-Original.pyi"
		os.rename(x,y)
		subprocess.call(["cp",y,path_output])


		command = ["pytype"]
		command.append("-k")
		command.append("-d")
		command.append("import-error")
		command.append(path_str + S[1])
		temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
		output,o2 = temp.communicate()
		output = str(output.decode('ascii','ignore'))
		o2 = str(o2.decode('ascii','ignore'))
		print("output = {}".format(output))
		x = path_pyi + E[-1] + "i"
		y = path_pyi + S[0] + "-Stripped.pyi"
		os.rename(x,y)
		subprocess.call(["cp",y,path_output])	

		subprocess.call(["cp",path_repo + S[1],path_output + "Files"])	
		
		line = fp.readline()
