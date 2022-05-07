import os

files = [ f.path+'/index.html' for f in os.scandir('.') if f.is_dir() ]

for index, file in enumerate(files):
	with open(file, 'r') as f:
		data = f.read()

	if 'a href="#"' in data:
		data = data.replace('a href="#"', 'a href="https://abdul-rehman-d.github.io/"')
		print(f'Fixed link in file {index}')

	if '>Your Name Here<' in data:
		data = data.replace('>Your Name Here<', '>Abdul Rehman Daniyal<')
		print(f'Fixed name in file {index}')

	with open(file, 'w') as f:
		f.write(data)

print('Done')