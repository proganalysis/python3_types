import subprocess
import os
import shutil
import glob
from operator import itemgetter
"""
Map from file_path -> List of [error row column]
"""
mypy = dict()
pytype = dict()
pylint = dict()

e_mypy = dict()
e_pytype = dict()
e_pylint = dict()

"""
mypy_pytype = dict()
pytype_mypy = dict()
mypy_pylint = dict()
pylint_mypy = dict()
"""

mypy_read_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/mypy/"
pytype_read_path = "/home/bew/Desktop/wp2/pytype_ULTIMATE/" 
pylint_read_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/pylint/"

T = True
F = False

do_mypy = T
do_pytype = T
do_pylint = T

L = 1
R = 28

mypy_noline = 0

if do_mypy:
	for ii in range(L,R):
		print(ii)
		mypy_read_path_mod = mypy_read_path + str(ii)
		with open(mypy_read_path_mod) as fp:
			for f in fp:
				t = f.strip()
				if "error:" in t:
					#print(t)
					if "cannot perform relative import" in t:
						continue
					if "Duplicate module named" in t:
						continue
					if "Are you missing an __init__.py?" in t:
						continue

					left = t.rfind("[")
					right = t.rfind("]")
					error_type = t[left+1:right]
					cut = t.find(" error: ")
					tt = t[cut:]
					ttt = t[:cut]
					x = ttt.split(':')
					#print("t = {}".format(t))
					#print("ttt = {}".format(ttt))
					#print("x = {}".format(x))
					if x[1] == '':
						mypy_noline += 1
						continue
					row = int(x[1])
					if(len(x) > 2):
						if x[2] == '':
							column = -1
						else:
							column = int(x[2])
					else:
						column = -1
					y = [error_type, row, column]
					#print(x[0])
					#print(y)

					# Might be able to make this more efficient
					if x[0] in mypy:
						z = mypy[x[0]]
						
						if y not in z:
							z.append(y)
							mypy[x[0]] = z

							if error_type in e_mypy:
								z = e_mypy[error_type]
								e_mypy[error_type] = z + 1
							else:
								e_mypy[error_type] = 1
						"""
						z.append(y)
						mypy[x[0]] = z
						"""
					else:
						z = [y]
						mypy[x[0]] = z

						if error_type in e_mypy:
							z = e_mypy[error_type]
							e_mypy[error_type] = z + 1
						else:
							e_mypy[error_type] = 1


	if 0:
		print("----------------------------------------------------------------")
		for m in mypy:
			zz = mypy[m]
			print(m)
			print(zz)
			#for z in zz:
			#	print(z)
	if 0:
		for m in sorted(e_mypy):
			print(m,e_mypy[m])

if do_pytype:
	for ii in range(L,R):
		print(ii)
		pytype_read_path_mod = pytype_read_path + str(ii)
		with open(pytype_read_path_mod) as fp:
			for f in fp:
				t = f.strip()
				if "[" in t and "]" in t and "line" in t and "File" in t:
					left = t.rfind("[")
					right = t.rfind("]")
					error_type = t[left+1:right]
					if "_K, _V" in error_type:
						continue
					if "_K, _V" in error_type:
						continue
					if "str]" in error_type:
						continue
					if "str, Any], tuple" in error_type:
						continue
					if "Any], int" in error_type:
						continue
					if "_KT, _VT" in error_type:
						continue
					if "list" == error_type or "str" == error_type:
						continue
					#print(t)
					#print(error_type)
					x = t.split(',')
					name = x[0].replace("File ","")
					name = name.replace("\"","")
					name = name.replace("/home/bew/archive/typed_project/","")
					row = x[1].replace(" line ","")
					#print("> {}".format(t))
					#print(">> {}".format(row))
					if len(x) <= 2 or ": " in row:
						row = row.split(':')
						row = row[0]
					if ") [" in row:
						row = row.split(')')
						row = row[0]
					row = int(row)
					#print(name)
					#print(row)
					column = -2
					y = [error_type, row, column]
					#print(error_type, row, column)
					#bew = int(row)

					if name in pytype:
						z = pytype[name]
						
						if y not in z:
							z.append(y)
							pytype[name] = z

							if error_type in e_pytype:
								z = e_pytype[error_type]
								e_pytype[error_type] = z + 1
							else:
								e_pytype[error_type] = 1
						"""
						z.append(y)
						pytype[name] = z
						"""
					else:
						z = [y]
						pytype[name] = z

						if error_type in e_pytype:
							z = e_pytype[error_type]
							e_pytype[error_type] = z + 1
						else:
							e_pytype[error_type] = 1
	if 0:
		for m in pytype:
			print(m)
			print(pytype[m])

if do_pylint:
	prev = ""
	for ii in range(L,R):
		print(ii)
		pylint_read_path_mod = pylint_read_path + str(ii)
		with open(pylint_read_path_mod) as fp:
			for f in fp:
				t = f.strip()
				if t.endswith(")"):
					if "Your code has been rated" in t:
						line = fp.readline()
						continue
					left = t.rfind("(")
					right = t.rfind(")")
					error_type = t[left+1:right]

					x = t.split(':')
					name = x[0].replace("File ","")
					name = name.replace("\"","")
					name = name.replace("/home/bew/archive/typed_project/","")
					good = 1
					if len(x) < 2:
						#print(prev)
						#print(t)
						good = 0
					else:
						if "sys.argv[0]" not in t:
							row = int(x[1])
							column = int(x[2])
						else:
							#print(prev)
							#print(t)
							good = 0
						
					#print(t)
					#print(name)
					#print(error_type)
					if "-" not in error_type:
						#print("ERRORRRRRRRRRRRRRRRRRRRR {}".format(error_type))
						good = 0

					if good == 1:
						y = [error_type, row, column]
						if name in pylint:
							z = pylint[name]
							
							if y not in z:
								z.append(y)
								pylint[name] = z

								if error_type in e_pylint:
									z = e_pylint[error_type]
									e_pylint[error_type] = z + 1
								else:
									e_pylint[error_type] = 1
							"""
							z.append(y)
							pylint[name] = z
							"""
						else:
							z = [y]
							pylint[name] = z

							if error_type in e_pylint:
								z = e_pylint[error_type]
								e_pylint[error_type] = z + 1
							else:
								e_pylint[error_type] = 1
				prev = t
	if 1:
		yy = []
		yy.append(["(facebook)buck/tools/build/modules/find_duplicate_classes_in_jars.py", ["syntax-error",221,101]])
		yy.append(["(facebook)buck/test/com/facebook/buck/android/testdata/android_project/java/com/resourceref/generator.py", ["syntax-error",12,74]])
		yy.append(["(ActiveState)code/recipes/Python/82347_pulse/recipe-82347.py",["syntax-error",14,23]])
		yy.append(["(ActiveState)code/recipes/Python/576837_Crop_PDF_File_with_pyPdf/recipe-576837.py",["syntax-error",32,682]])
		yy.append(["(ActiveState)code/recipes/Python/576483_Convert_Subnetmask_CIDR_notatidotdecimal/recipe-576483.py",["syntax-error",6,32]])
		yy.append(["(quarkslab)irma/probe/extras/tools/nsrl/import_nsrl.py",["syntax-error",24,35]])
		yy.append(["(gnachman)iTerm2/tests/ranges.py",["syntax-error",8,80]])
		yy.append(["(oilshell)oil/Python-2.7.13/Tools/unicode/mkstringprep.py",["syntax-error",117,304]])
		yy.append(["(WZQ1397)automatic-repo/python/FileSystem/backupSmallFileToTarToLocal.py",["syntax-error",42,177]])
		yy.append(["(mapsme)omim/data/benchmarks/tk_results_viewer.py",["syntax-error",251,60]])
		yy.append(["(ric2b)Vivaldi-browser/chromium/tools/win/pe_summarize.py",["syntax-error",69,55]])
		yy.append(["(ric2b)Vivaldi-browser/chromium/remoting/tools/extract_android_native_lib.py",["syntax-error",16,64]])
		yy.append(["(ric2b)Vivaldi-browser/chromium/remoting/tools/remove_spaces.py",["syntax-error",13,30]])
		yy.append(["(ric2b)Vivaldi-browser/chromium/third_party/android_platform/development/scripts/stack.py",["syntax-error",50,19]])
		yy.append(["(endlessm)chromium-browser/third_party/angle/third_party/deqp/src/scripts/cppcheck.py",["syntax-error",155,26]])
		yy.append(["(endlessm)chromium-browser/third_party/angle/third_party/deqp/src/scripts/log/log_to_xml.py",["syntax-error",186,35]])
		yy.append(["(endlessm)chromium-browser/third_party/angle/third_party/deqp/src/external/vulkancts/scripts/verify_submission.py",["syntax-error",79,55]])
		yy.append(["(mlperf)training_results_v0.6/Fujitsu/benchmarks/resnet/implementations/mxnet/3rdparty/mkldnn/scripts/generate_mkldnn_debug.py",["syntax-error",192,316]])

		for yyy in yy:
			name = yyy[0]
			y = yyy[1]
			if name in pylint:
				z = pylint[name]
				z.append(y)
				pylint[name] = z
			else:
				z = [y]
				pylint[name] = z
			error_type = y[0]
			if error_type in e_pylint:
				z = e_pylint[error_type]
				e_pylint[error_type] = z + 1
			else:
				e_pylint[error_type] = 1

	if 0:
		for m in pylint:
			print(m)
			print(pylint[m])






def compare(X, Y, id, does):
	if does == 0:
		return

	result = dict()
	for m in X:
		if m in Y:
			xx = X[m]
			yy = Y[m]
			#print("> {}".format(m))
			#print(xx)
			#print(yy)

			# THIS IS INEFFICIENT (how to spell?)
			for x in xx:
				for y in yy:
					if x[1] == y[1]:
						if x[0] in result:
							z = result[x[0]]
							r = []
							#print(">x = {}".format(x))
							#print(">y = {}".format(y))
							#print(">Z = {}".format(z))
							incr = 0
							for u in z:
								if y[0] == u[0]:
									incr = 1
									r.append([y[0], u[1] + 1])
								else:
									r.append(u)
							if incr == 0:
								r.append([y[0], 1])
							#print(">R = {}".format(r))
							result[x[0]] = r
						else:
							z = [[y[0], 1]]
							result[x[0]] = z

	if id == 1:
		print("----- Mypy -> Pytype -----")
	elif id == 2:
		print("----- Pytype -> Mypy -----")
	elif id == 3:
		print("----- Mypy -> Pylint -----")
	elif id == 4:
		print("----- Pylint -> Mypy -----")
	elif id == 5:
		print("----- Pytype -> Pylint -----")
	elif id == 6:
		print("----- Pylint -> Pytype -----")

	for c in result:
		a = result[c]
		a.sort(key=itemgetter(1,0), reverse=True)
		result[c] = a

	for c in sorted(result):
		#print(c, result[c])
		total = -1
		if id == 1 or id == 3:
			total = e_mypy[c]
		elif id == 2 or id == 5:
			total = e_pytype[c]
		elif id == 4 or id == 6:
			total = e_pylint[c]
		use = 0
		for r in result[c]:
			use += r[1]
		print("{} {}/{}".format(c,use,total))
		print(" ",result[c])

	print("")




compare(mypy, pytype, 1, 0)
compare(pytype, mypy, 2, 0)
compare(mypy, pylint, 3, 0)
compare(pylint, mypy, 4, 0)
compare(pytype, pylint, 5, 0)
compare(pylint, pytype, 6, 0)

def compareThree(X, Y, Z, id, does):
	if does == 0:
		return

	result = dict()
	for m in X:
		if m in Y:
			if m in Z:
				xx = X[m]
				yy = Y[m]
				vv = Z[m]
				#print("> {}".format(m))
				#print(xx)
				#print(yy)

				# THIS IS INEFFICIENT (how to spell?)
				for x in xx:
					for y in yy:
						for v in vv:
							if x[0] == "operator" and y[0] == "unsupported-operands" and v[0] == "invalid-unary-operand-type":
								print(m, x, y, v)
							if x[1] == y[1] and y[1] == v[1]:
								#print(">x = {}".format(x))
								#print(">y = {}".format(y))
								#print(">v = {}".format(v))
								if x[0] in result:
									z = result[x[0]]
									r = []
									#print(">x = {}".format(x))
									#print(">y = {}".format(y))
									#print(">Z = {}".format(z))
									incr = 0
									for u in z:
										if y[0] == u[0] and v[0] == u[1]:
											incr = 1
											r.append([y[0], v[0], u[2] + 1])
										else:
											r.append(u)
									if incr == 0:
										r.append([y[0], v[0], 1])
									#print(">R = {}".format(r))
									result[x[0]] = r
								else:
									z = [[y[0],v[0],1]]
									result[x[0]] = z

	if id == 1:
		print("----- Mypy -> [Pytype, Pylint] -----")
	elif id == 2:
		print("----- Pytype -> Mypy -----")
	elif id == 3:
		print("----- Mypy -> Pylint -----")
	elif id == 4:
		print("----- Pylint -> Mypy -----")
	elif id == 5:
		print("----- Pytype -> Pylint -----")
	elif id == 6:
		print("----- Pylint -> Pytype -----")

	for c in result:
		a = result[c]
		a.sort(key=itemgetter(2,1,0), reverse=True)
		result[c] = a

	for c in sorted(result):
		#print(c, result[c])
		"""
		print(c)
		print(" ",result[c])
		"""
		total = -1
		if id == 1 or id == 3:
			total = e_mypy[c]
		elif id == 2 or id == 5:
			total = e_pytype[c]
		elif id == 4 or id == 6:
			total = e_pylint[c]
		use = 0
		for r in result[c]:
			use += r[2]
		print("{} {}/{}".format(c,use,total))
		print(" ",result[c])

	print("Not in any:")
	for i in e_mypy:
		if i not in result:
			print(i)
		

	print("")

compareThree(mypy, pytype, pylint, 1, 1)







"""
if do_mp_pt:
	for m in mypy:
		if m in pytype:
			xx = mypy[m]
			yy = pytype[m]
			#print("> {}".format(m))
			#print(xx)
			#print(yy)

			# THIS IS INEFFICIENT (how to spell?)
			for x in xx:
				for y in yy:
					if x[1] == y[1]:
						if x[0] in mypy_pytype:
							z = mypy_pytype[x[0]]
							r = []
							#print(">x = {}".format(x))
							#print(">y = {}".format(y))
							#print(">Z = {}".format(z))
							incr = 0
							for u in z:
								if y[0] == u[0]:
									incr = 1
									r.append([y[0], u[1] + 1])
								else:
									r.append(u)
							if incr == 0:
								r.append([y[0], 1])
							#print(">R = {}".format(r))
							mypy_pytype[x[0]] = r
						else:
							z = [[y[0], 1]]
							mypy_pytype[x[0]] = z

	print("----- Mypy -> Pytype -----")
	for c in mypy_pytype:
		a = mypy_pytype[c]
		a.sort(key=itemgetter(1,0), reverse=True)
		mypy_pytype[c] = a
	#for c in mypy_pytype:
	for c in sorted(mypy_pytype):
		print(c, mypy_pytype[c])
	print("")

	for m in pytype:
		if m in mypy:
			xx = pytype[m]
			yy = mypy[m]
			for x in xx:
				for y in yy:
					if x[1] == y[1]:
						if x[0] in pytype_mypy:
							z = pytype_mypy[x[0]]
							r = []
							incr = 0
							for u in z:
								if y[0] == u[0]:
									incr = 1
									r.append([y[0], u[1] + 1])
								else:
									r.append(u)
							if incr == 0:
								r.append([y[0], 1])
							pytype_mypy[x[0]] = r
						else:
							z = [[y[0], 1]]
							pytype_mypy[x[0]] = z

	print("----- Pytype -> Mypy -----")
	for c in pytype_mypy:
		a = pytype_mypy[c]
		a.sort(key=itemgetter(1,0), reverse=True)
		pytype_mypy[c] = a
	#for c in pytype_mypy:
	for c in sorted(pytype_mypy):
		print(c, pytype_mypy[c])
	#print(com[c])
"""




#print("Mypy: Error messages with no line number = {}".format(mypy_noline))