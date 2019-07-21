import os
for root, dirs, files in os.walk(".", topdown=True):
	if '.\\.git' in root:
		continue
	print root