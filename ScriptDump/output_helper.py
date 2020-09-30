path = "/home/bew/Desktop/wp2/Output/ignoreMissingImport/var-annotated"
with open(path) as fp:
	line = fp.readline()
	while line:
		t = line.strip()
		if not "Need type annotation for" in t:
			print(t)
		line = fp.readline()
