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
total_errors = 0

global_Map = dict()
M = dict()
Errors = dict()
perType = dict()
byType = dict()

prev = ""
notMypy = 0
var_annotated_hint = 0
var_annotated_no_hint = 0
var_annotated_dict = 0
var_annotated_list = 0
var_annotated_set = 0

union_attr_None = 0
eiei = 0

temp_count_1 = 0
temp_count_2 = 0
temp_count_3 = 0
temp_count_4 = 0

deppu = dict()

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
					#print(pprev)
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

				if "LogLevel" in tt:
					print (tt)

				if 0:
					vv = tt.replace("[" + error_type + "]", "")
					lll = len(vv)Invalid type annotation '<instance of module>' for title [invalid-annotation]
					#print(vv)
					kk = 0
					dep = -1
					for jj in range(0, lll):
						if vv[jj] == '[':
							kk += 1
						elif vv[jj] == ']':
							kk -= 1
						dep = max(dep, kk)
					#print(dep)
					oo = str(dep)
					if dep != 0:
						if oo not in deppu:
							deppu[oo] = [t]
						else:
							rr = deppu[oo]
							rr.append(t)
							deppu[oo] = rr

				if error_type == "KEKW":
					vv = tt.replace("hint:","???")
					vv = vv.replace("tkinter","?")
					vv = vv.replace("__init__","?")
					vv = vv.replace("abstract","?")
					vv = vv.replace("oint","?")
					vv = vv.replace("print","?")
					vv = vv.replace("strategy","?")
					print(vv)

					eg = "Union"
					if eg in vv:
						print(vv)
						temp_count_1 += 1
					if eg + "[" in vv:
						temp_count_2 += 1

					if "Any" in vv:
						temp_count_3 += 1
					if "None" in vv:
						temp_count_4 += 1




				if error_type == "attr-defined":
					if "has no attribute" not in tt:
						print(tt)

				if error_type == "var-annotated":
					if "(hint:" in tt:
						var_annotated_hint += 1
					else:
						var_annotated_no_hint += 1

					if "Dict[" in tt:
						var_annotated_dict += 1
					if "List[" in tt:
						var_annotated_list += 1
					if "Set[" in tt:
						var_annotated_set += 1
					if "Dict[<type>, <type>]" in tt:
						eiei += 1
					# print(tt)

				if error_type == "union-attr":
					if "\"None\" of" in tt:
						union_attr_None += 1
					else:
						tt = tt
						#print(tt)
					#print(tt)

				if error_type == "misc":
					#print(tt)
					#if "Relative import climbs" not in tt:
					#	if "Bracketed expression" not in tt:
					#		print(tt)
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

				total_errors += 1
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

				if error_type in perType:
					amount = perType[error_type]
					perType[error_type] = amount + 1
				else:
					perType[error_type] = 1
					
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

print("temp_count_1 = {}".format(temp_count_1))
print("temp_count_2 = {}".format(temp_count_2))
print("temp_count_3 = {}".format(temp_count_3))
print("temp_count_4 = {}\n".format(temp_count_4))

if 0:
	print("GLOBAL SUMMARY: Total repo = {}".format(total_repos))
	for x in sorted(global_Map, key = global_Map.get, reverse = True):
		# print("  {} {}".format(x,global_Map[x]))
		print("  {} {} {}".format(x,global_Map[x],perType[x]))

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
	print("Total errors = {}".format(total_errors))
	print("var-annotated hint = {}, no hint = {}".format(var_annotated_hint, var_annotated_no_hint))
	print("var-annotated dict = {}, list = {}, set = {},  eiei = {}".format(var_annotated_dict, var_annotated_list, var_annotated_set, eiei))
	print("union_attr_None = {}".format(union_attr_None))



#path_catag = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
path_catag = "/home/bew/Desktop/wp2/byType/mypy/"
if 0:
	print("\n\n")
	for x in byType:
		s = path_catag + x
		fp = open("%s" % s, "w");
		y = byType[x]
		for z in y:
			z = z + "\n"
			fp.writelines(z)
		fp.close()

path_catag = "/home/bew/Desktop/wp2/byDepth/"
if 0:
	for x in deppu:
		print(x)
		if int(x) > 2:
			s = path_catag + x
			fp = open("%s" % s, "w");
			for y in deppu[x]:
				#print(y)
				z = y + "\n"
				fp.writelines(z)
			fp.close()