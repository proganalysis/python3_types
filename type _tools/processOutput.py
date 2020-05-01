#read_path = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
#read_path = "/home/bew/Desktop/wp2/ManyFlags/"
read_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/mypy/"
not_mypy_write_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/notMypy"
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

prev = ""
notMypy = 0

fnp = open(not_mypy_write_path, 'w')

for ii in range(1,28):
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
					#print("{} {}".format(ii,prev))
					#print(ii)
					#print(t)
					empty += 1
				if hasSomething == 0 or b1 > 0 or b2 > 0:
					notMypy += 1
					pprev = prev.replace("[RRepo]","")
					print(pprev)
					fnp.write("%s\n" % pprev)
				hasSomething = 0
				prev = t
				#print(total_repos)
				if b1 > 0 and b2 > 0:
					b3 += 1
				b1 = 0
				b2 = 0
				stop += 1
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
				if "Duplicate module named" in t:
					duplicate_module += duplicate_module_helper
					duplicate_module_helper = min(0,duplicate_module_helper)
					b1 += 1
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

fnp.close()
print("GLOBAL SUMMARY: Total repo = {}".format(total_repos))
for x in sorted(global_Map, key = global_Map.get, reverse = True):
	print("  {} {}".format(x,global_Map[x]))

print("\n\n")
print("(misc) - Number of repo with these errors. One repo can have more than 1 type")
print("{}: Duplicate module named 'xxx' (also at 'PATH/TO/ANOTHER/MODULE/xxx')".format(duplicate_module))
print("{}: No parent module -- cannot perform relative import".format(relative_import))
print("{}: Bracketed expression '[...]' is not valid as a type".format(bracket_expression))
print("{}: Relative import climbs too many namespaces".format(climb_too_many))
print("{}: Incompatible import of 'aaa' (imported name has type 'yyy', local name has type 'zzz'".format(incompatible_import))
print(" ")
print("{}: Success: no issues found in #NUMBER source files".format(success))
print("Incompatible types in assignment (expression has type \"None\" = {}".format(expression_none))

print("NotMypy = {}".format(notMypy))
print("Empty = {}".format(empty))

#path_catag = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
path_catag = "/home/bew/Desktop/wp2/ManyFlags/"
if 0:
	print("\n\n")
	for x in Errors:
		s = path_catag + x
		fp = open("%s" % s, "w");
		y = Errors[x]
		for z in y:
			z = z + "\n"
			fp.writelines(z)
		fp.close()

