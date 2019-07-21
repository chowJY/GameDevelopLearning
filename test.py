import os
for root, dirs, files in os.walk(".", topdown=True):
	if '.\\.git' in root:
		continue
	for dirr in dirs:
		print dirr