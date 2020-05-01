import subprocess
import os
import shutil
import glob

#cmd = ['echo', 'I like potatos']
#proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
#write_path = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
#write_path = "/home/bew/Desktop/wp2/afterImport/mypy4/"

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

SSS = set(["1"])

repo_num = 0
file_num = 0
ex_num = 0

LIM = 28
bew = dict()

#for ii in range(1,28):
for ii in range(1,LIM):
	path_repo_list_num = path_repo_list + str(ii)
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
			repo_num += 1

			full_repo_path = mainrepo + repo	
			print("> ({}){} {}".format(ii, count, full_repo_path))
			all_files = glob.glob(full_repo_path + "/**/*.py", recursive = True)
			#command = command + all_files
			#command.append(full_repo_path)
			per_repo = 0
			SSS.clear()
			for ff in all_files:
				#print(ff)
				namee = ff.split("/")[-1]
				#print(namee)
				if namee not in SSS:
					SSS.add(namee)
					per_repo += 1
					file_num += 1
					command.append(ff)
				#print("_{}".format(ff))
			#	command.append
			bew[full_repo_path] = per_repo		


	fp.close()









G_REPO = 0
G_FILE = 0

read_path = "/home/bew/Desktop/wp2/afterImport/mypy3/"
total_repos = 0
stop = 0

relative_import = 0
relative_import_helper = 1
duplicate_module = 0
duplicate_module_helper = 1
expression_none = 0
incompatible_import = 0
incompatible_import_helper = 1
bracket_expression = 0	
bracket_expression_helper = 1
climb_too_many = 0
climb_too_many_helper = 1
success = 0

b1 = 0
b2 = 0
b3 = 0
hasSomething = 1
empty = 0

global_Map = dict()
M = dict()
Errors = dict()
buak = 0
current = 0

for ii in range(1,LIM):
	read_path_num = read_path + str(ii)
	with open(read_path_num) as fp:
		line = fp.readline()
		while line:
			if line == '\n':
				# print("----")
				line = fp.readline()
				continue
			t = line.strip()
			t_no_path = t.replace("/home/bew/archive/typed_project/","")
			# print(">{}".format(t))
			#Typpete
			#if "(loopspace)microbit" in t:
			#	print(t)
			if "[RRepo]" in t:

				relative_import_helper = 1
				duplicate_module_helper = 1
				incompatible_import_helper = 1
				bracket_expression_helper = 1
				climb_too_many_helper = 1
				total_repos += 1
				if hasSomething == 0:
					#print(ii)
					#print(t)
					#print(current)
					buak -= current
					current = 0
					empty += 1
				hasSomething = 0
				#print(total_repos)
				if b1 > 0 and b2 > 0:
					b3 += 1
				b1 = 0
				b2 = 0
				stop += 1

				mag = t
				magg = mag.replace("[RRepo]","/home/bew/archive/typed_project/")
				print("{} {}".format(bew[magg],magg))
				buak += bew[magg]
				bad = 1
				current = bew[magg]


				for x in M:
					# print("__{} {}".format(x,M[x]))
					if x in global_Map:
						amount = global_Map[x]
						global_Map[x] = amount + 1
					else:
						global_Map[x] = 1
				# print("Next")
				M.clear()
			if "Success: no issues found in" in t:
				hasSomething += 1
				success += 1
			if " error: " in t:
				hasSomething += 1

				left = t.rfind("[")
				right = t.rfind("]")
				error_type = t[left+1:right]

				cut = t.find(" error: ")
				tt = t[cut:]
				if error_type == "misc":
					#print(tt)
					tt = tt

				if "cannot perform relative import" in t:
					relative_import += relative_import_helper
					relative_import_helper = min(0,relative_import_helper)
					b2 += 1
					#print(current)
					buak -= current
					curent = 0
				if "Duplicate module named" in t:
					duplicate_module += duplicate_module_helper
					duplicate_module_helper = min(0,duplicate_module_helper)
					b1 += 1
					#print(current)
					buak -= current
					curent = 0
				if "Incompatible import of" in t:
					incompatible_import += incompatible_import_helper
					incompatible_import_helper = min(0,incompatible_import_helper)
				if "Bracketed expression" in t:
					bracket_expression += bracket_expression_helper
					bracket_expression_helper = min(0,bracket_expression_helper)
				if "Relative import climbs too many namespaces" in t:
					climb_too_many += climb_too_many_helper
					climb_too_many_helper = min(0,climb_too_many_helper)

				if "Incompatible types in assignment (expression has type \"None\"" in t:
					expression_none += 1
					# print(tt)


				# print(error_type)
				if error_type in M:
					amount = M[error_type]
					M[error_type] = amount + 1
					Errors[error_type].append(t_no_path)
				else:
					M[error_type] = 1
					if error_type not in Errors:
						Errors[error_type] = []
					Errors[error_type].append(t_no_path)

			else:
				line = fp.readline()
				continue

			line = fp.readline()
			if stop == -1:
				break
	for x in M:
		if x in global_Map:
			amount = global_Map[x]
			global_Map[x] = amount + 1
		else:
			global_Map[x] = 1
	M.clear()

if hasSomething == 0:
	empty += 1






print(repo_num)
print(file_num)
print(ex_num) 
print("Buak = {}".format(buak))

print("{}: Duplicate module named 'xxx' (also at 'PATH/TO/ANOTHER/MODULE/xxx')".format(duplicate_module))
print("{}: No parent module -- cannot perform relative import".format(relative_import))
print("{}: Empty".format(empty))

