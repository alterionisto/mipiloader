import shutil
import os, sys
import string
import time

def validate(answer):
	if answer not in ["yes", "no"]:
		raise Exception("Invalid input")

drive = ""
marked = False
make_mark = False
source = False
"""
for letter in string.ascii_lowercase:
	if os.path.isfile(os.path.join(letter + ":\\", "mark.mark")):
		drive = letter
		marked = True
		break 

choise = "no"
if (drive != ""):
	choise = raw_input("Found mark.mark on %s. Use it? (yes, no): " % drive)
validate(choise)
if choise == "no":
	disk = raw_input("Destination disk: ")
drive = drive + ":\\"
purge = raw_input("Purge before copying? (yes, no): ")
validate(purge)
if marked == False:
	make_mark = raw_input("Create mark.mark file in root? (yes, no): ")
	"""
#source = input("Source folder: ")
source = r"F:\music"
print("Lift off")
ret = 0
copied = 0
current = 0
file_list = []
print("Gathering files")
for (path, dirs, files) in os.walk(source.encode(sys.getfilesystemencoding())):
	for file in files:
		file_list.append(file)
print(file_list[:10])
for x in file_list[-5:]:
	print(type(x))
	print(x)
	print(str(x))
	#print(x.decode(sys.getfilesystemencoding()))

exit()
"""
while ret == 0:
	print "\r Copied: %i, current: %s" % (copied, I),

	ret = os.system("copy file %s" )
	if not ret:
		copied += 1
print "Finished copying"
if make_mark:
	print "Creating mark.mark file"
	pass """
