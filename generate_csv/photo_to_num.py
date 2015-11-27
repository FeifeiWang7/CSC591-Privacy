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
		if arr[10] == "default":
			wd.write(line.replace(arr[10],"0"))
		elif arr[10] == "false":
			wd.write(line.replace(arr[10],"1"))
		elif arr[10] == "true":
			wd.write(line.replace(arr[10],"2"))
		elif arr[10].startswith('http', 0, 4):
			wd.write(line.replace(arr[10],"3"))
		else:
			print line
			wd.write(line)
	fd.close()
	wd.close()
if __name__ == '__main__':
	import sys
	replace_url(sys.argv[1],sys.argv[2])
