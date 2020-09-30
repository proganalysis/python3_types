import subprocess
import os
import shutil
import glob

path_repo_list = "/home/bew/Desktop/wp2/typed-repos-divided/"
mainrepo = "/home/bew/archive/typed_project/"
write_path = "/home/bew/Desktop/wp2/FilteredRepoNFiles/pylint/"
path_file_list = "/home/bew/Desktop/wp2/FilteredRepoNFiles/Files/"


g_command = ["shopt","-s","globstar"]
#g_temp = subprocess.Popen(g_command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)

count = 0
count_inside = 0
os.chdir("/home/bew/archive/typed_project")


# for ii in range(1,28):
for ii in range(10,11):
	path_repo_list_num = path_repo_list + str(ii)
	write_path_num = write_path + str(ii)
	fpWrite = open(write_path_num, 'w')
	count_inside += 1
	with open(path_repo_list_num) as fp:
		line = fp.readline()
		while line:
			count += 1
			repo = line.strip()
			repo.replace("(","\(")
			repo.replace(")","\)")
			line = fp.readline()

			#if "aiohttp-spyne" not in repo:
			#	continue

			#os.chdir("/home/bew/archive/typed_project/" + repo)
			#print(os.getcwd())

			command = ["pylint"]
			command.append("-d")
			command.append("I , R , C , W , F")
			fpWrite.write("[RRepo]%s\n" % repo)

			full_repo_path = mainrepo + repo	
			print("> ({}){} {}".format(ii, count, full_repo_path))
			#all_files = glob.glob(full_repo_path + "/**/*.py", recursive = True)
			#command = command + all_files
			#command.append(full_repo_path)

			with open(path_file_list + repo + ".txt") as fpp:
				for ff in fpp:
					x = ff.strip()
					command.append(x)

			temp = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
			output,o2 = temp.communicate()
			output = str(output.decode('ascii','ignore'))
			o2 = str(o2.decode('ascii','ignore'))
			#print("1 = {}".format(output))
			#print("2 = {}".format(o2))
			output = output.split('\n')
			for oo in output:
				#print("< {}".format(oo))
				fpWrite.write("%s\n" % oo)
			
			#break;

	fp.close()
	fpWrite.close()




#    def test_split(self):
#        s = 'hello world'
#        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
#        with self.assertRaises(TypeError):
#            s.split(2)
            