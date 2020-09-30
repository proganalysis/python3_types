import re

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

fnp = open(not_mypy_write_path, 'w')

raw_user_defined = dict()

def fput(x):
	if x in raw_user_defined:
		y = raw_user_defined[x]
		raw_user_defined[x] = y + 1
	else:
		raw_user_defined[x] = 1

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

				#print(tt)
				if 1:
					if error_type == "arg-type":
						a1 = tt.split("has incompatible")[1]
						a2 = re.findall('"([^"]*)"', a1)
						fput(a2[0])
						if len(a2) > 1:
							fput(a2[1])

					if error_type == "assignment":
						if "Cannot assign to a method" not in tt:
							a1 = tt.split("Incompatible ")[1]
							a2 = re.findall('"([^"]*)"', a1)
							for ij in range(len(a2)):
								fput(a2[ij])

					if error_type == "attr-defined":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						if len(a2) == 2:
							fput(a2[0])

					if error_type == "call-arg":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						if "of" in a1:
							fput(a2[len(a2)-1])

					if error_type == "call-overload":
						if "matches argument" in tt:
							a1 = tt.split("matches argument")[1]
							a2 = re.findall('"([^"]*)"', a1)
							for ij in range(len(a2)):
								fput(a2[ij])

					if error_type == "dict-item":
						a1 = tt.split("has incompatible")[1]
						a2 = re.findall('"([^"]*)"', a1)
						for ij in range(len(a2)):
							fput(a2[ij])

					if error_type == "exit-return":
						a2 = re.findall('"([^"]*)"', tt)
						fput(a2[0])

					if error_type == "index":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						for ij in range(len(a2)):
							fput(a2[ij])	

					if error_type == "list-item":
						a1 = tt.split("has incompatible")[1]
						a2 = re.findall('"([^"]*)"', a1)
						for ij in range(len(a2)):
							fput(a2[ij])	

					if error_type == "misc":
						if "Incompatible types in" in tt:
							a1 = tt.split("Incompatible types in")[1]
							a2 = re.findall('"([^"]*)"', a1)
							for ij in range(len(a2)):
								if ij == 0:
									continue
								fput(a2[ij])

					if error_type == "operator":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						if "No overload variant" in a1:
							for ij in range(len(a2)):
								if ij == 0:
									continue
								fput(a2[ij])
						else:
							for ij in range(len(a2)):
								fput(a2[ij])	
								
					if error_type == "override":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						if "Return type " in tt:
							fput(a2[0])
							fput(a2[2])
						elif "defines the argument" in tt:
							fput(a2[len(a2)-1])

					if error_type == "return-value":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						for ij in range(len(a2)):
							fput(a2[ij])
							
					if error_type == "type-arg":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						for ij in range(len(a2)):
							fput(a2[ij])

					if error_type == "union-attr":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						fput(a2[0])
						fput(a2[1])
		
					if error_type == "valid-newtype":
						a1 = tt.split(" error: ")[1]
						a2 = re.findall('"([^"]*)"', a1)
						for ij in range(len(a2)):
							fput(a2[ij])






				if error_type == "attr-defined":
					if "has no attribute" not in tt:
						tt = tt
						#print(tt)

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
print("var-annotated dict = {}, list = {}, set = {}".format(var_annotated_dict, var_annotated_list, var_annotated_set))
print("union_attr_None = {}".format(union_attr_None))


processed = dict()
banned = ["Any", "int", "float", "boold", "str", "List", "Tuple", "Dict", "Optional", "Callble", "Union", "TypeVar", "Generic", "Set", "None", ">", "...", 
"<nothing>", "<subclass of", "<union: 9 items>"]

nubb = 0
if 1:
	for x in sorted(raw_user_defined, key = raw_user_defined.get, reverse = True):
		#print("  {} {}".format(x,raw_user_defined[x]))
		nubb += raw_user_defined[x]

		a = x
		b = re.split('\[|\]|,|\(|\)|\'', a)
		for y in range(len(b)):
			c = b[y].strip()
			if c != "" and c not in banned:
				#print(c)
				if c not in processed:
					processed[c] = 1


print(nubb)
print(len(raw_user_defined))

for x in sorted(processed.keys()):
	print(x)

print(len(processed))

if 1:
	fp = open("/home/bew/Desktop/wp2/Notes&Stats/Processed_Mypy_types.txt", "w")
	for x in sorted(processed.keys()):
		z = x + "\n"
		fp.writelines(z)

if 0:
	fp = open("/home/bew/Desktop/wp2/Notes&Stats/Raw_Mypy_types.txt", "w")
	for x in sorted(raw_user_defined, key = raw_user_defined.get, reverse = True):
		z = x + " " + str(raw_user_defined[x]) + "\n"
		fp.writelines(z)	





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

