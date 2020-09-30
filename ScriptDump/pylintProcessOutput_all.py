#read_path = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
read_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/pylint(typecheck_update)/"
#read_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/pylint/"
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
perType = dict()
byType = dict()

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

			if t.endswith(")"):
				if "Your code has been rated" in t:
					line = fp.readline()
					continue
				left = t.rfind("(")
				right = t.rfind(")")
				error_type = t[left+1:right]

				cut = t.find(" error: ")
				#tt = t[cut:]
				#if error_type == "misc":
					#print(tt)
					#tt = tt


				#print(error_type)
				if error_type in M:
					amount = M[error_type]
					M[error_type] = amount + 1
					Errors[error_type].append(t_no_path)
				else:
					M[error_type] = 1
					if error_type not in Errors:
						Errors[error_type] = []
					Errors[error_type].append(t_no_path)

				if error_type in perType:
					amount = perType[error_type]
					perType[error_type] = amount + 1
				else:
					perType[error_type] = 1


				if "-" in error_type:
					if error_type in byType:
						byType[error_type].append(t_no_path)
					else:
						byType[error_type] = [t_no_path]					

			else:
				line = fp.readline()
				continue

			line = fp.readline()
			if stop == -1:
				break

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
	print("  {} {} {}".format(x,global_Map[x],perType[x]))




print("GLOBAL SUMMARY: Total repo = {}".format(total_repos))
print("SUCCESS repo = {}".format(success))


path_catag = "/home/bew/Desktop/wp2/byType/pylint/"
if 0:
	print("\n\n")
	for x in byType:
		s = path_catag + x
		#print(s)
		fp = open("%s" % s, "w");
		y = byType[x]
		for z in y:
			z = z + "\n"
			fp.writelines(z)
		fp.close()
