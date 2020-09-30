import subprocess
import os
import shutil
import glob

path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
write_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/mypy/"
path_file_list = "/home/bew/Desktop/wp2/FilteredRepoNFiles/Files/"

os.chdir("/home/bew/archive/typed_project")

g_command = ["shopt","-s","globstar"]

count = 0
repo_count = 0
file_count = 0

DDD = dict()
FFF = dict()

empty_repo =  0
#for ii in range(1,28):

for ii in range(1,2):
	path_repo_list_num = path_repo_list + str(ii)
	write_path_num = write_path + str(ii)
	#write_path_num = write_path + str(ii) + "55555555"
	fpWrite = open(write_path_num, 'w')
	with open(path_repo_list_num) as fp:
		line = fp.readline()
		while line:	
			count += 1
			repo_count += 1
			repo = line.strip()
			repo.replace("(","\(")
			repo.replace(")","\)")
			line = fp.readline()

			if repo != "(viaict)viaduct":
				continue

			command = ["mypy"]
			command.append("--show-error-codes")
			command.append("--namespace-packages")
			command.append("--ignore-missing-imports")
			command.append("--show-column-numbers")
			# command.append("--allow-redefinition")
			fpWrite.write("[RRepo]%s\n" % repo)

			full_repo_path = mainrepo + repo	
			print("> ({}){} {}".format(ii, count, full_repo_path))
			#all_files = glob.glob(full_repo_path + "/**/*.py", recursive = True)
			ggg = 0
			with open(path_file_list + repo + ".txt") as fpp:
				for ff in fpp:
					x = ff.strip()
					command.append(x)
					ggg += 1
			if ggg == 0:
				empty_repo += 1
			"""
			fpWrite.write("mypy --config-file mypy.ini ")
			for uu in command:
				uu = uu.replace("/home/bew/archive/typed_project/(viaict)viaduct/", "")
				if "app" in uu:
					fpWrite.write("%s " % uu)
			fpWrite.write("\n\n")
			"""
			temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
			output,o2 = temp.communicate()
			output = str(output.decode('ascii','ignore'))
			o2 = str(o2.decode('ascii','ignore'))
			anything = 0
			#print("1 = {}".format(output))
			print("2 = {}".format(o2))
			output = output.split('\n')
			for oo in output:
				#print("< {}".format(oo))
				anything += 1
				fpWrite.write("%s\n" % oo)
			#for ooo in o2:
			#	fpWrite.write("%s\n" % ooo)
			if anything == 0:
				print(output)
				print(o2)

		

	fpWrite.close()
print(empty_repo)