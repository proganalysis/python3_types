import subprocess
import os
import shutil
import glob
import validators

gitUrl = {}
tools = {}
numPython = {}
avgAnn = {}
passMypy = []
passPytype = []

with open("/home/bew/Desktop/wp2/deletePassMypy") as f1:
	line = f1.readline()
	while line:
		ll = line.strip()
		passMypy.append(ll)
		line  = f1.readline()
print(len(passMypy))

with open("/home/bew/Desktop/wp2/deletePassPytype") as f2:
	line = f2.readline()
	while line:
		ll = line.strip()
		passPytype.append(ll)
		line  = f2.readline()
print(len(passPytype))

with open("/home/bew/Desktop/wp2/deeletee3") as f3:
	line = f3.readline()
	while line:
		ll = line.strip()
		uu = ll.split(":::")
		if uu[0] in gitUrl.keys():
			print("BUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
		else:
			gitUrl[uu[0]] = uu[1]
		line  = f3.readline()
print(len(gitUrl))

with open("/home/bew/Desktop/wp2/counter_scripts/numFiles") as f4:
	line = f4.readline()
	while line:
		ll = line.strip()
		uu = ll.split(":")
		if uu[0] in numPython.keys():
			print("BUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
		else:
			numPython[uu[0]] = uu[1]
		line = f4.readline()
print(len(numPython))

with open("/home/bew/Desktop/wp2/counter_scripts/numAvg") as f5:
	line = f5.readline()
	while line:
		ll = line.strip()
		uu = ll.split(":")
		if uu[0] in avgAnn.keys():
			print("BUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
		else:
			avgAnn[uu[0]] = uu[1]
		line = f5.readline()
print(len(avgAnn))


tools["(kalaspuff)tomodachi"] = "MYPY, flake8"
tools["(aio-libs)aiozmq"] = "pycodestyle, pyflakes"
tools["(thorgate)tg-utils"] = "flake8"
tools["(viaict)viaduct"] = "MYPY, PYLINT, flake8, pep8, pyflakes, pycodestyle"
tools["(PyPlanet)PyPlanet"] = "PyYAML"
tools["(openai)kubernetes-ec2-autoscaler"] = "MYPY, PyYAML"
tools["(XayOn)katcr"] = "PYLINT"
tools["(CloverHealth)pycon2017"] = "PYLINT"
tools["(statgen)pheweb"] = "flake8"
tools["(adaptive-learning)robomission"] = "PYLINT, pyparsing"
tools["(channelcat)sanic"] = "MYPY, PYLINT, flake8"
tools["(katajakasa)aiohttp-spyne"] = "MYPY, flake8"
tools["(knights-lab)SHOGUN"] = "PyYAML"
tools["(carpyncho)feets"] = "PYLINT"
tools["(yutiansut)QUANTAXIS"] = "PYLINT"
tools["(ahawker)scratchdir"] = "MYPY, PYLINT, flake8, pep8"
tools["(drootnar)asynckraken"] = "MYOY, flake8, pep8"
tools["(clearlinux)autospec"] = "flake8"
tools["(abiosoft)dotfiles"] = "PYLINT"
tools["(samuelcolvin)pydantic"] = "MYPY, PYLINT, (mentioned PYTYPE in 2 issues)"
tools["(MasuqaT-NET)BlogExamples"] = "(have MYPY's cache and PYCHARM's .idea file)"
tools["(CenterForOpenScience)SHARE"] = "flake8"
tools["(funkyfuture)inxs"] = "flake8"

print(len(tools))



path = "/home/bew/archive/typed_project/"
path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
write_path = "/home/bew/Desktop/wp2/deleteeplsV2"
path_file_list = "/home/bew/Desktop/wp2/FilteredRepoNFiles/Files/"

count = 0
fpWrite = open(write_path, 'w')

for ii in range(1,28):
	path_repo_list_num = path_repo_list + str(ii)
	#write_path_num = write_path + str(ii)
	#write_path_num = write_path + str(ii) + "55555555"
	#fpWrite = open(write_path_num, 'w')
	with open(path_repo_list_num) as fp:
		line = fp.readline()
		while line:	
			count += 1
			repo = line.strip()

			#repo.replace("(","\(")
			#repo.replace(")","\)")
			line = fp.readline()

			aa = repo.split(')')
			org = aa[0].replace("(","")
			rep = aa[1]

			w_rep = "<td>" + rep + "</td>"
			w_org = "<td>" + org + "</td>"
			if gitUrl[repo] == "N/A":
				w_url = "<td>" + gitUrl[repo] + "</td>"
			else:
				w_url = "<td><a href=\"" + gitUrl[repo] + "\" target=\"_blank\">" + gitUrl[repo] + "</a></td>"
			if repo in tools.keys():
				w_tools = "<td>" + tools[repo] + "</td>"
			else:
				if count <= 50:
					w_tools = "<td>" + "-" + "</td>"
				else:
					w_tools = "<td>" + "?" + "</td>"
			w_num = "<td>" + numPython[repo] + "</td>"
			w_avg = "<td>" + str(round(float(avgAnn[repo]),2)) + "</td>"
			if repo in passMypy:
				w_mypy = "<td>" + "Yes" + "</td>"
			else:
				w_mypy = "<td>" + "No" + "</td>"
			if repo in passPytype:
				w_pytype = "<td>" + "Yes" + "</td>"
			else:
				w_pytype = "<td>" + "No" + "</td>"

			fpWrite.write("%s\n" % "<tr>")
			fpWrite.write("%s\n" % w_rep)
			fpWrite.write("%s\n" % w_org)
			fpWrite.write("%s\n" % w_url)
			fpWrite.write("%s\n" % w_tools)
			fpWrite.write("%s\n" % w_num)
			fpWrite.write("%s\n" % w_avg)
			fpWrite.write("%s\n" % w_mypy)
			fpWrite.write("%s\n" % w_pytype)
			fpWrite.write("%s\n" % "</tr>")


print(count)



