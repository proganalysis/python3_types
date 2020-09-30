import subprocess
import os
import shutil
import glob
import validators

path = "/home/bew/archive/typed_project/"
bubu = ["https://github.com/theheros/kbengine",
		"https://github.com/opensyllabus/osp-api"]


path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
write_path = "/home/bew/Desktop/wp2/deleteepls"
path_file_list = "/home/bew/Desktop/wp2/FilteredRepoNFiles/Files/"

count = 0
fpWrite = open(write_path, 'w')

for ii in range(1,2):
	path_repo_list_num = path_repo_list + str(ii)
	write_path_num = write_path + str(ii)
	#write_path_num = write_path + str(ii) + "55555555"
	#fpWrite = open(write_path_num, 'w')
	with open(path_repo_list_num) as fp:
		line = fp.readline()
		while line:	
			count += 1
			repo = line.strip()
			repo.replace("(","\(")
			repo.replace(")","\)")
			line = fp.readline()

			aa = repo.split(')')
			org = aa[0].replace("(","")
			rep = aa[1]

			link = "https://github.com/" + org + "/" + rep
			if 0:
				print(link)
				command = ["git"]
				command.append("ls-remote")
				command.append("-h")
				command.append(link)

				temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
				output,o2 = temp.communicate()
				output = str(output.decode('ascii','ignore'))
				o2 = str(o2.decode('ascii','ignore'))
				print(output)
				print("---")
				print(os)
				print("=============")
			#print("<tr>")
			fpWrite.write("%s\n" % "<tr>")
			#print("<td>" + rep + "</td>")
			fpWrite.write("%s" % "<td>" + rep + "</td>")
			fpWrite.write("\n")
			#print("<td>" + org + "</td>")
			fpWrite.write("%s" % "<td>" + org + "</td>")
			fpWrite.write("\n")
			if link in bubu:
				#print("<td>N/A</td>")
				fpWrite.write("%s\n" % "<td>N/A</td>")
			else:
				#print("<td><a href=\"" + link + " target=\"_blank\">" + link + "</a></td>")
				fpWrite.write("%s" % "<td><a href=\"" + link + "\" target=\"_blank\">" + link + "</a></td>")
				fpWrite.write("\n")
			#print("<td>?</td>")
			fpWrite.write("%s\n" % "<td>?</td>")
			#print("</tr>")
			fpWrite.write("%s\n" % "</tr>")


print(count)










if 0:
	path = "/home/bew/archive/typed_project/"
	res = []
	eee = 0
	for root,dirs,files in os.walk(path, topdown=True):
		if eee == 0:
		    depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
		    if depth == 0:
		    	if not files:
		    		print("bug")
		    	res = dirs
			    #print(depth)
			    #print(root)
			    #print(dirs)
			    #print(files)
			    #rint("-------")
		eee += 1
		break
	    #if depth == 0:
	    #    # We're currently two directories in, so all subdirs have depth 3
	    #    res += [os.path.join(root, d) for d in dirs]
	    #    dirs[:] = [] # Don't recurse any deeper

	print(res)
	print(len(res))