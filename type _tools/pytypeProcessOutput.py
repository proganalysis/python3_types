#read_path = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
read_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/pytype/"
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


global_Map = dict()
M = dict()
Errors = dict()

#for ii in range(1,28):
for ii in range(1,28):
	print(ii)
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
				#print(total_repos)
				
				stop += 1
				if len(M) == 0:
					success += 1
				for x in M:
					# print("__{} {}".format(x,M[x]))
					if x in global_Map:
						amount = global_Map[x]
						global_Map[x] = amount + 1
					else:
						global_Map[x] = 1
				# print("Next")
				M.clear()
				line = fp.readline()
				continue

			#if "Success: no issues found in" in t:
			#	success += 1
			if "[" in t:
				if "]" in t:
					if "line" in t:
						left = t.rfind("[")
						right = t.rfind("]")
						error_type = t[left+1:right]
						if "/" not in error_type:
							#print(error_type)

							if 1:
								if "jinja" in error_type:
									line = fp.readline()
									continue
								if "bool" in error_type:
									line = fp.readline()
									continue
								if "_T" in error_type:
									line = fp.readline()
									continue
								if "_K, _V" in error_type:
									line = fp.readline()
									continue
								if "str]" in error_type:
									line = fp.readline()
									continue
								if "str, Any], tuple" in error_type:
									line = fp.readline()
									continue
								if "Any], int" in error_type:
									line = fp.readline()
									continue
								if "_KT, _VT" in error_type:
									line = fp.readline()
									continue
								if "types.TracebackType" in error_type:
									line = fp.readline()
									continue
								if ":" in error_type:
									line = fp.readline()
									print("> {}".format(error_type))
									continue
								if "-" not in error_type:
									line = fp.readline()
									print("> {}".format(error_type))
									continue



							if error_type in M:
								amount = M[error_type]
								M[error_type] = amount + 1
								Errors[error_type].append(t_no_path)
							else:
								M[error_type] = 1
								if error_type not in Errors:
									Errors[error_type] = []
								Errors[error_type].append(t_no_path)

			line = fp.readline()

	if len(M) == 0:
		success += 1
	for x in M:
		if x in global_Map:
			amount = global_Map[x]
			global_Map[x] = amount + 1
		else:
			global_Map[x] = 1
	M.clear()



print("GLOBAL SUMMARY: Total repo = {}".format(total_repos))
for x in sorted(global_Map, key = global_Map.get, reverse = True):
	print("  {} {}".format(x,global_Map[x]))



print("GLOBAL SUMMARY: Total repo = {}".format(total_repos))
print("SUCCESS repo = {}".format(success))

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

