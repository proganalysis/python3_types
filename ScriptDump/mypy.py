import subprocess
import os
import shutil
import glob

#cmd = ['echo', 'I like potatos']
#proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
#write_path = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
write_path = "/home/bew/Desktop/wp2/afterImport/mypy/"

#cmd = ['mypy', 
#'/home/bew/archive/repos/0Chencc/CTFCrackTools/Lib/test/test_urllib2net.py', 
#'--ignore-missing-imports', 
#'--no-error-summary', 
#'--no-strict-optional', 
#'--no-warn-no-return', 
#'--allow-untyped-globals', 
#'--allow-redefinition', 
#'--linecount-report', 
# --warn-unreachable ?????????//
#'/home/bew/Desktop']

#proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#o, e = proc.communicate()

#print('Output: ' + o.decode('ascii'))
#print('Error: '  + e.decode('ascii'))
#print('code: ' + str(proc.returncode))
# mypy --show-error-codes --namespace-packages /home/bew/archive/typed_project/\(kalaspuff\)tomodachi/*.py /home/bew/archive/typed_project/\(kalaspuff\)tomodachi/**/*.py


g_command = ["shopt","-s","globstar"]
#g_temp = subprocess.Popen(g_command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)

count = 0
count_inside = 0
# for ii in range(1,28):
current_path = os.getcwd()
print(current_path)
os.chdir("/home/bew/archive/typed_project")
current_path = os.getcwd()
print(current_path)

for ii in range(1,28):
	path_repo_list_num = path_repo_list + str(ii)
	write_path_num = write_path + str(ii)
	fpWrite = open(write_path_num, 'w')
	count_inside += 1
	with open(path_repo_list_num) as fp:
		line = fp.readline()
		while line:
			count += 1
			repo = line.strip()
			repo.replace("(","\(")
			repo.replace(")","\)")
			line = fp.readline()

			#if "aiohttp-spyne" not in repo:
			#	continue

			#os.chdir("/home/bew/archive/typed_project/" + repo)
			#print(os.getcwd())

			command = ["mypy"]
			command.append("--show-error-codes")
			command.append("--namespace-packages")
			command.append("--ignore-missing-imports")
			# command.append("--allow-redefinition")
			fpWrite.write("[RRepo]%s\n" % repo)

			full_repo_path = mainrepo + repo	
			print("> ({}){} {}".format(ii, count, full_repo_path))
			all_files = glob.glob(full_repo_path + "/**/*.py", recursive = True)
			#command = command + all_files
			#command.append(full_repo_path)
			for ff in all_files:
				#print("_{}".format(ff))
				command.append(ff)
			temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
			output,o2 = temp.communicate()
			output = str(output.decode('ascii','ignore'))
			o2 = str(o2.decode('ascii','ignore'))
			#print("1 = {}".format(output))
			#print("2 = {}".format(o2))
			
			output = output.split('\n')
			for oo in output:
				#print("< {}".format(oo))
				fpWrite.write("%s\n" % oo)

	fp.close()
	fpWrite.close()


