import os

paths = [ f.path for f in os.scandir('.') if f.is_dir() ]

objs = []

for path in paths[:-1]:
	obj = {}
	obj['name'] = ' '.join(path.split('_')[1].split('-')).title()
	obj['folderName'] = path[2:]
	objs.append(obj)
	
print(objs)