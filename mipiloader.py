import shutil
import os, sys
import platform
import string
import time
import random
import ctypes
import pprint
from argparse import ArgumentParser

def get_free_space(folder):
	""" Return folder/drive free space (in bytes)
	"""
	if platform.system() == 'Windows':
		free_bytes = ctypes.c_ulonglong(0)
		ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), 
			None, None, ctypes.pointer(free_bytes))
		return free_bytes.value
	else:
		return os.statvfs(folder).f_bfree

def size_format(num):
    for x in ['bytes','KiB','MiB','GiB']:
        if num < 1024.0 and num > -1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TiB')

parser = ArgumentParser(description="Media device random filler")
parser.add_argument("-p", "--purge", action="store_true", dest="purge",
	help="purge the destination directory")
parser.add_argument("-r", "--reserve", dest="reserve", type=int,
	help="reserve x KiB of free space on device")
parser.add_argument("-e", "--extensions", dest="extensions", nargs="*",
	default="mp3 flac aac wav".split(),
	help="acceptable file extensions, default is mp3, flac, aac, wav")
parser.add_argument("source")
parser.add_argument("destination")
args = parser.parse_args()
pprint.pprint(args.__dict__)
source = args.source #.encode(sys.getfilesystemencoding())
destination = args.destination #.encode(sys.getfilesystemencoding())
if not os.path.isdir(source):
	raise SystemExit("source is not a directory")
if not os.path.isdir(args.destination):
	print("creating destination folder")
	os.makedirs(args.destination)
if args.reserve and int(args.reserve) <= 0:
	raise SystemExit("reserve value is invalid")

dev_free = get_free_space(destination)
print("free space:", size_format(dev_free))
if args.reserve and dev_free < args.reserve:
	print("impossible to reserve given amount")

if args.purge:
	print("cleaning ", destination)
	for (p, d, files) in os.walk(destination)
		for f in files:
			os.remove(os.path.join(p, f))
file_list = []
[file_list.append(os.path.join(path, f))
	for (path, dirs, files) in os.walk(source)
	for f in files
	if os.path.splitext(f)[1][1:] in args.extensions]
print("{} files found".format(len(file_list)))

current = ret = copied = 0
while True:
	current = random.choice(file_list)
	dev_free = get_free_space(destination)
	if args.reserve and (dev_free - os.path.getsize(current)) < args.reserve:
		print("reached reserve limit")
		break
	if dev_free < os.path.getsize(current):
		print("device is full")
		break
	print("copying", os.path.basename(current))
	shutil.copy(current, destination)
	copied += 1	
	file_list.remove(current)
	if not file_list:
		print("copied everything")
		break
