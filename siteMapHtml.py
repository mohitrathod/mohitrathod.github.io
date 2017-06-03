from os import listdir, makedirs
from os.path import isfile, join, dirname, realpath
import re

class Node:
    text = None
    url = None
    child = None

currPath = dirname(realpath(__file__))

navPath = currPath + '\\nav'


def processFiles(currentPath, inputFiles, dataTree):
    for file in inputFiles:
        dataTree.text = file
        dataTree.url = currentPath + '\\' + file



def getFilesOfDirs(currentDir, inputDirs, dataTree):
    for dir in inputDirs:
        if dir == '.git':
            continue
        filesT = [f for f in listdir(currentDir + '\\' + dir) if isfile(join(currentDir + '\\' + dir, f))]
        processFiles(currentDir + '\\' + dir, filesT, dataTree)
        getFilesOfDirs(currentDir + '\\' + dir,
                       [f for f in listdir(currentDir + '\\' + dir) if not isfile(join(currentDir + '\\' + dir, f))], dataTree)


# processFiles(mypath, files)

dataTree = Node()

getFilesOfDirs(navPath,
               [f for f in listdir(navPath) if not isfile(join(navPath, f))], dataTree)


print(dataTree)


