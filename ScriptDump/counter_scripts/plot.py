import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from operator import itemgetter

#read_path = "/home/bew/Desktop/wp2/counter_scripts/sample"
read_path = "/home/bew/Desktop/wp2/counter_scripts/raw"
write_path_1 = "/home/bew/Desktop/wp2/counter_scripts/numFiles"

fpWrite = open(write_path_1, 'w')

L = []
num_repo = 0
ei = []
cl = {}

noww = ""

# num_anno/num_files/anno_per_file
with open(read_path) as fp:
	line = fp.readline()
	while line:
		ll = line.strip()
		if ll == "=====":
			line = fp.readline()
			ll = line.strip()
			s = ll.split(":")
			if int(s[1]) == 0:
				ei = s
			q = [int(s[1]), int(s[2]), float(float(s[1])/float(s[2]))]
			L.append(q)
			print(s)
			num_repo += 1
			oo = s[0] + ":" + str(int(s[2]))
			fpWrite.write("%s\n" % oo)
			#if num_repo > 1000:
			#	break
		else:
			s = ll.split(":")
			anno = int(s[0])
			freq = int(s[1])
			if anno in cl.keys():
				cl[anno] += freq
			else:
				cl[anno] = freq

		line = fp.readline()

L = sorted(L, key = itemgetter(2), reverse = True)
d = []
e = []
oo = 1
for l in L:
	e.append(str(oo))
	d.append(l[2])
	oo += 1
print("Num repo: ", num_repo)
print(L)
#print(d)
#print(cl)

maxx = -1
for x in cl.keys():
	if maxx < x:
		maxx = x

print(maxx)
f = []
for i in range(0,maxx+1):
	if i in cl.keys():
		f.append([i,cl[i]])
	else:
		f.append([i,0])
#print(f)

if False:
	df2 = pd.DataFrame(f)
	df2.to_excel("out3.xlsx",index = False, header = False)

if False:
	#df1 = pd.DataFrame([['a','b'],['c','d']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
	df1 = pd.DataFrame(d)
	df1.to_excel("out2.xlsx",index = False, header = False)



if False:
	#np.random.seed(444)
	#np.set_printoptions(precision=3)

	#d = np.random.laplace(loc=15, scale=3, size=500)
	#print(d)
	# An "interface" to matplotlib.axes.Axes.hist() method
	#n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
	#d = [2,3,5,4,1,2,2,3]
	#num_repo = 8
	#e = ["a","c","b"]
	#d = [4,5,6]
	print(len(e),len(d))
	plt.bar(x = e, height = d, width = 0.1, color='#0504aa')

	#plt.grid(axis='y', alpha=0.75)
	plt.xlabel('Value')
	plt.ylabel('Frequency')
	plt.title('My Very Own Histogram')
	#plt.text(23, 45, r'$\mu=15, b=3$')
	#maxfreq = n.max()
	# Set a clean upper y-axis limit.
	#plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
	plt.savefig("fig.png")


