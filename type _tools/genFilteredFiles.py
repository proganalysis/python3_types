import subprocess
import os
import shutil
import glob

def getFiles(path: str) -> list:
	all_files = []
	for r,d,f in os.walk(path):
		for file in f:
			if '.py' in file:
				if '.pyc' not in file:
					all_files.append(os.path.join(r,file))
	return all_files

path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
write_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/Files/"
write_path_stat = "/home/bew/Desktop/wp2/FilteredRepoNFiles/Stats"


g_command = ["shopt","-s","globstar"]

count = 0
repo_count = 0
file_count = 0

DDD = dict()
FFF = dict()

#for ii in range(1,28):

fpStat = open(write_path_stat, 'w')
for ii in range(1,28):
	print(ii)
	path_repo_list_num = path_repo_list + str(ii)
	#write_path_num = write_path + str(ii)
	#fpWrite = open(write_path_num, 'w')
	with open(path_repo_list_num) as fp:
		line = fp.readline()
		while line:
			count += 1
			repo_count += 1
			repo = line.strip()
			repo.replace("(","\(")
			repo.replace(")","\)")
			line = fp.readline()

			fpW = open(write_path + repo + ".txt", 'w')

			#fpWrite.write("[RRepo]%s\n" % repo)

			full_repo_path = mainrepo + repo	
			#print("> ({}){} {}".format(ii, count, full_repo_path))
			#all_files = glob.glob(full_repo_path + "/**/*.py", recursive = True)
			all_files = getFiles(full_repo_path)
			DDD.clear()
			FFF.clear()
			remaining_files = 0
			for ff in all_files:
				exc = 0
				with open(ff) as f7:
					for line7 in f7:
						u = line7.strip()
						if "from . import" in u:
							exc = 1 
						if "from .. import" in u:
							exc = 1 
						if "from ... import" in u:
							exc = 1 
						if "from .... import" in u:
							exc = 1 
				if exc == 1:
					continue
				#print(ff)
				namee = ff.split("/")[-1]
				depth = ff.count('/')
				if "__init__.py" in namee:
					fpW.write("%s\n" % ff)
					remaining_files += 1
					continue
				#print(namee)
				if namee not in DDD:
					DDD[namee] = depth
					FFF[namee] = ff
				else:
					depth_2 = DDD[namee]
					#print(ff)
					if depth < depth_2:
						#print("YIKE {}:{} {}:{}".format(depth,ff,depth_2,FFF[namee]))
						DDD[namee] = depth
						FFF[namee] = ff
				#print("_{}".format(ff))
			#	command.append(ff)
			for fff in FFF:
				fpW.write("%s\n" % FFF[fff])
				#command.append(FFF[fff])
			fpW.close()

			total_files = len(all_files)
			remaining_files += len(FFF)
			file_count += remaining_files
			#print("{} {} {} {}".format(remaining_files,total_files,(remaining_files/total_files),repo))
			fpStat.write("%d %d %f %s\n" % (remaining_files,total_files,(remaining_files/total_files),repo))
			

		

fpStat.close()

print(repo_count)
print(file_count)