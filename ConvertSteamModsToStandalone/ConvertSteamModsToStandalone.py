import os
import shutil
from pathlib import Path

steamCSDir = Path("C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\255710")
workingDir = Path("C:\\Users\\louis\\Desktop\\cstemp")

# Set up the working directories and copy mods and assets
if workingDir.exists:
	try:
		shutil.rmtree(workingDir)
		pass
	except:
		pass

shutil.copytree(steamCSDir, workingDir)

def isExcluded(name):
	if "." in name:
		return True

	exclusionList = [
		"0Harmony",
		"CimTools"
	]

	if name in exclusionList:
		return True

	return False

for dirName in workingDir.iterdir():
	dir = Path(dirName)

	if dir.is_dir():

		# Take care of a few special cases
		if (dir / "1ParallelRoadTool.dll").exists():
			dir.rename(workingDir / "ParallelRoadTool")
			continue

		if dir.name == "1959183067":
			fileToMove = dir / "CSURLoader.dll"
			if fileToMove.exists():
				newAssetDir = workingDir / fileToMove.stem
				os.mkdir(newAssetDir)
				fileToMove.rename(newAssetDir / fileToMove.name)

		for fileName in dir.iterdir():
			file = Path(fileName)
			
			# Rename the folders with DLLS to the first DLL that meets the criteria.

			if file.suffix == ".dll" and not isExcluded(file.stem):
				dir.rename(workingDir / file.stem)
				break

print("Done.")