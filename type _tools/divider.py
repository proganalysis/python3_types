import os 
import shutil

path = "typed-repos-test-REAL"
# f1 = open("typed-repos-test-REAL","r")
# f2 = open(r"/home/bew/Desktop/wp2/typed-repos-divided/
ss = "/home/bew/Desktop/wp2/typed-repos-divided/"
count = 0
cc = 1;
s = ss + "0"
f1 = open("%s" % s, "w");
with open(path) as fp:
	line = fp.readline()
	while line:
		#print("> {} {}".format(count,line.strip()))
		if count % 100 == 0:
			f1.close()
			s = ss + str(cc)
			f1 = open("%s" % s, "w")
			cc += 1			
			print("> {} {}".format(count,line.strip()))
		count += 1 
		t = line.strip() + "\n"
		f1.writelines(t);
		line = fp.readline()


f1.close()
