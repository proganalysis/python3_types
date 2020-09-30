import subprocess
import os
import shutil
import glob
import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
#uuu = "https://github.com/kalaspuff/tomodachi/blob/master/mypy.ini"
write_path = "/home/bew/Desktop/wp2/deeletee3"

count = 0
found = 0
fpWrite = open(write_path, 'w')

for ii in range(1,28):
	path_repo_list_num = path_repo_list + str(ii)
	#write_path_num = write_path + str(ii)
	#write_path_num = write_path + str(ii) + "55555555"
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

			nnn  = "(" + org + ")" + rep

			#link = "https://github.com/" + org + "/" + rep + "/blob/"
			link = "https://github.com/" + org + "/" + rep
			ll = link

			print(count, found, ll)
			req = Request(ll)
			tor = 0
			try:
				response = urlopen(req)
			except HTTPError as e:
				print("HTTP Error:", e.code)
				tor = 1
			except URLError as e:
				print("URL Error:", e.reason)
				tor = 1
			else:
				print("FOUND!")
				found += 1
				oo = nnn + ":::" + ll
				fpWrite.write("%s\n" % oo)
				tor = 0
			if tor == 1:
				oo = nnn + ":::" + "N/A"
				fpWrite.write("%s\n" % oo)

			time.sleep(1)
	time.sleep(10)

print("Total mypy.ini at top level = ", found)


if 0:
	req = Request(uuu)
	try:
		response = urlopen(req)
		print("yay")
		print(response)
	except HTTPError as e:
		print("HTTP Error: ", e.code)
	except URLError as e:
		print("URL Error: ", e.reason)
	else:
		print("Error")