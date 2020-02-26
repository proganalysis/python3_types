#read_path = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/"
read_path = "/home/bew/Desktop/wp2/pylint/"
total_repos = 0
stop = 0


global_Map = dict()
M = dict()
Errors = dict()
global_bad = 0
global_line2long = 0
bad = 0
line2long =0  
#for ii in range(1,28):
for ii in range(1,8):
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
				if bad > 0:
					global_bad += 1
					global_line2long += 1
				else:
					if line2long > 0:
						global_line2long += 1
				total_repos += 1
				bad = 0
				line2long = 0
				#print(total_repos)
				
			if "trailing-whitespace" in t:
				bad += 1
			if "trailing-newlines" in t:
				bad += 1
			if "bad-whitespace" in t:
				bad += 1
			if "mixed-indentation" in t:
				bad += 1
			if "bad-continuation" in t:
				bad += 1
			if "superfluous-parens" in t:
				bad += 1
			if "multiple-statements" in t:
				bad += 1
			if "len-as-condition" in t:
				bad += 1
			if "line-too-long" in t:
				line2long += 1

			line = fp.readline()
			if stop == -1:
				break

if bad > 0:
	global_bad += 1


print("GLOBAL SUMMARY: Total repo = {}".format(total_repos))
print("Bad repo = {}".format(global_bad))
print("Bad repo including (line-too-long) = {}".format(global_line2long))
