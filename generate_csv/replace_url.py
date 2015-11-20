from is_human import is_human
def replace_url(inputFile,outputFile):
	fd = open(inputFile, 'r')
	wd = open(outputFile, 'w')
	wd.write(fd.readline())
	for line in fd:
		arr = line.split(',')
		if(len(arr)<11):
			wd.write(line)
			continue
		if arr[9] == "False":
			if arr[10].startswith('http', 0, 4):
				tmp = arr[10][:-6]
			  	wd.write(line.replace(arr[10],is_human(tmp)))
			else:
				wd.write(line)
		elif arr[9] == "True":
			wd.write(line.replace(arr[10],"default"))
		else:
			wd.write(line)
	fd.close()
	wd.close()
if __name__ == '__main__':
	import sys
	replace_url(sys.argv[1],sys.argv[2])
