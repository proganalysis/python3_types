import subprocess
import os
import shutil
import glob
import ast
from collections import namedtuple

Import = namedtuple("Import", ["module", "name", "alias"])
error_files = 0

def get_imports(path):
	with open(path) as fh:
		try:
			root = ast.parse(fh.read(), path)
		except:
			global error_files 
			error_files += 1
			print("Error ast.parse in " + path)
			return

	for node in ast.iter_child_nodes(root):
		if isinstance(node, ast.Import):
			module = []
		elif isinstance(node, ast.ImportFrom):
			if node.module is None:
				continue
			module = node.module.split('.')
		else:
			continue

		for n in node.names:
			yield Import(module, n.name.split('.'), n.asname)


path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
write_path = "/home/bew/Desktop/wp2/xxx/"

global_Map = dict()
M = dict()
temp_Map = dict()

g_command = ["shopt","-s","globstar"]

count = 0
count_inside = 0
total_files = 0

current_path = os.getcwd()
print(current_path)
os.chdir("/home/bew/archive/typed_project")
current_path = os.getcwd()
print(current_path)

# for ii in range(1,28):
for ii in range(1,28):
	path_repo_list_num = path_repo_list + str(ii)
	#write_path_num = write_path + str(ii)
	#fpWrite = open(write_path_num, 'w')
	count_inside += 1
	with open(path_repo_list_num) as fp:
		for line in fp:
			count += 1
			repo = line.strip()
			repo.replace("(","\(")
			repo.replace(")","\)")

			full_repo_path = mainrepo + repo	
			print("> ({}){} {}".format(ii, count, full_repo_path))
			all_files = glob.glob(full_repo_path + "/**/*.py", recursive = True)
			for ff in all_files:
				#print(ff)
				total_files += 1
				for imp in get_imports(ff):
					#print(imp)
					x = getattr(imp, "module")
					#print(x)
					#print(len(x))
					z = ""
					if len(x) == 0:
						y = getattr(imp, "name")
						z = y[0]
					else:
						z  = x[0]
					#print(z)

					if z in M:
						amount = M[z]
						M[z] = amount + 1
					else:
						M[z] = 1
					if z in temp_Map:
						amount = temp_Map[z]
						temp_Map[z] = amount + 1
					else:
						temp_Map[z] = 1

			for x in temp_Map:
				if x in global_Map:
					amount = global_Map[x]
					global_Map[x] = amount + 1
				else:
					global_Map[x] = 1
			temp_Map.clear()

			#break
			
	fp.close()
	#fpWrite.close()

print("Total repos = " + str(count))
print("Total files = " + str(total_files) + ", # files with ast.parse error = "  + str(error_files))

limit = 1000
writing = 1

i = 0
write_path = "/home/bew/Desktop/wp2/import/byFiles"
if writing:
	fp = open("%s" % write_path, "w");
print("By files: Number of files that import these modules")
for x in sorted(M, key = M.get, reverse = True):
	i += 1
	#print("  {} {}".format(x,M[x]))
	if writing:
		z = x + " " + str(M[x]) + "\n"
		fp.writelines(z)
	#if i >= limit:
		#break
if writing:
	fp.close()



i = 0
write_path2 = "/home/bew/Desktop/wp2/import/byRepos"
if writing:
	fp2 = open("%s" % write_path2, "w");
print("By repo: Number of repos that import these modules in at least 1 file")
for x in sorted(global_Map, key = global_Map.get, reverse = True):
	i += 1
	#print("  {} {}".format(x,global_Map[x]))
	if writing:
		z = x + " " + str(global_Map[x]) + "\n"
		fp2.writelines(z)
	#if i >= limit:
		#break
if writing:
	fp2.close()


write_path3 = "/home/bew/Desktop/wp2/import/stats"
if writing:
	fp3 = open("%s" % write_path3, "w");
	z = "Total repos = " + str(count) + "\n"
	fp3.writelines(z)
	z = "Total files = " + str(total_files) + ", # files with ast.parse error = "  + str(error_files) + "\n"
	fp3.writelines(z)
	z = "By files: Number of files that import these modules" + "\n"
	fp3.writelines(z)
	z = "By repo: Number of repos that import these modules in at least 1 file" + "\n"
	fp3.writelines(z)