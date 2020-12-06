import os
dirnum = 0
filenum = 0
path = './notes'

for lists in os.listdir(path):
    sub_path = os.path.join(path, lists)
    print(sub_path)
    if os.path.isfile(sub_path):
        filenum = filenum+1
    elif os.path.isdir(sub_path):
        dirnum = dirnum+1

print('dirnum: ',dirnum)
print('filenum: ',filenum)


with open('README.md') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
	if line.startswith("- There are"):
		idx = i
		break
		
if idx:
	lines[idx] = '- There are totally <big>**{}**</big> solutions in this repo.\n'.format(dirnum)
	f = open('README.md','w')
	res = ""
	for line in lines:
		res += line
	f.write(res)
	f.close()

