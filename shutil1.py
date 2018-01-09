# Regularely copy a folder to a destination folder.
# 
# Author: E A Rockland
# 07.01.2017

import shutil, datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sourceFolder = "Adobe"
destinationFolder = "FolderIn"
destinationArrays = list()

def LengthOfDestinationArrayAfterAdding(_destFolder):
	destinationArrays.append(_destFolder)
	return len(destinationArrays)

def GetDatedNameForBackupFolder():
	# Setup new destinationFolder
	destinationFolder = "Backup {0}".format(datetime.datetime.now().date())
	return destinationFolder
	

def Timer():
	sceduler = BlockingScheduler()
	sceduler.add_job(Copy, 'interval', args=[destinationFolder], hours=0.001)
	sceduler.start()

def Copy(_destinationFolder):
	try:
		_destinationFolder = GetDatedNameForBackupFolder()
		shutil.copytree(sourceFolder, _destinationFolder)
	except Exception as e:
		validDestination = "{0}-{1}".format(_destinationFolder, LengthOfDestinationArrayAfterAdding(_destinationFolder))
		shutil.copytree(sourceFolder, validDestination)
		#print(len(destinationArrays))
		print("Destination folder: \"{0}-\"{1}\" is already existing".format(_destinationFolder, len(destinationArrays)-1))
		print("Copying to destination \"{0}\"... ".format(validDestination))
		pass
	else:
		pass
	finally:		
		print("All is well and successful! \"{0}\" is copied!".format(_destinationFolder))
		pass

Timer()

#Copy(GetDatedNameForBackupFolder())
