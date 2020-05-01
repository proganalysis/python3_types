import subprocess
import os
import shutil
import glob

#cmd = ['echo', 'I like potatos']
#proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
#write_path = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
write_path = "/home/bew/Desktop/wp2/TypeVar/TypeVarCounter"

g_command = ["shopt","-s","globstar"]

count = 0
count_inside = 0
# for ii in range(1,28):
current_path = os.getcwd()
print(current_path)
os.chdir("/home/bew/archive/typed_project")
current_path = os.getcwd()
print(current_path)

repo_with_TypeVar = 0
global_total_files = 0
global_files_with_TypeVar = 0

fpWrite = open(write_path, 'w')

#for ii in range(1,28):
for ii in range(1,28):
	path_repo_list_num = path_repo_list + str(ii)
	write_path_num = write_path + str(ii)
	# fpWrite = open(write_path_num, 'w')
	count_inside += 1
	with open(path_repo_list_num) as fp:
		line = fp.readline()
		while line:
			count += 1
			repo = line.strip()
			repo.replace("(","\(")
			repo.replace(")","\)")
			line = fp.readline()

			reee = repo
			repo_no_path = reee.replace("/home/bew/archive/typed_project/","")

			# fpWrite.write("[RRepo]%s\n" % repo)

			full_repo_path = mainrepo + repo	
			all_files = glob.glob(full_repo_path + "/**/*.py", recursive = True)


			files_with_TypeVar = 0

			for ff in all_files:
				#print("_{}".format(ff))
				#command.append(ff)
				TypeVar_count = 0
				global_total_files += 1

				with open(ff) as fpp:
					linee = fpp.readline()
					while linee:
						lll = linee.strip()
						if(lll.find('TypeVar') != -1):
							TypeVar_count += 1
						linee = fpp.readline()
				fpp.close()

				if(TypeVar_count != 0):
					global_files_with_TypeVar += 1
					files_with_TypeVar += 1

			if(files_with_TypeVar != 0):
				repo_with_TypeVar += 1
				fpWrite.write("%d %s\n" % (files_with_TypeVar, repo_no_path))
			print("> ({}){} {}. Files with TypeVar = {}. Total repo with TypeVar = {}".format(ii, count, full_repo_path, files_with_TypeVar, repo_with_TypeVar))


	fp.close()
	# fpWrite.close()

fpWrite.close()
print("Repo with TypeVar = {}".format(repo_with_TypeVar))
print("Total number of files = {}".format(global_total_files))
print("Files with TypeVar = {}".format(global_files_with_TypeVar))
