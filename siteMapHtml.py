from os import listdir, makedirs
from os.path import isfile, join, dirname, realpath
import re


class URLDetails:
    name = None
    link = None
    child = []


currPath = dirname(realpath(__file__))
navPath = currPath + '\\nav'

template = open(currPath + '/nav/static/' + "sitemap.html", 'r').read()
allListing = []


def processFiles(currentPath, inputFiles):
    for file in inputFiles:
        url = currentPath + '\\' + file
        ptn = '\\\\nav(.*)'
        matches = re.findall(ptn, url)
        if len(matches) > 0:
            url = matches[0]
            url = url.replace('\\', '/')
            print(url)
            allListing.append(url)


def getFilesOfDirs(currentDir):
    filesT = [f for f in listdir(currentDir) if isfile(join(currentDir, f))]
    processFiles(currentDir, filesT)

    inputDirs = [f for f in listdir(currentDir) if not isfile(join(currentDir, f))]

    for dir in inputDirs:
        if dir == '.git' or dir == 'static':
            continue
        # filesT = [f for f in listdir(currentDir + '\\' + dir) if isfile(join(currentDir + '\\' + dir, f))]
        # processFiles(currentDir + '\\' + dir, filesT)
        getFilesOfDirs(currentDir + '\\' + dir)


# processFiles(mypath, files)

baseRoot = URLDetails()

def findNodeAndAdd(childs, strData):
    for child in childs:
        if child.name in strData:
            child.childs.append(strData)


def checkAndAdd(strData):
    if strData.count('/') > 1:
        findNodeAndAdd(baseRoot.child, strData)
    else:
        newChild = URLDetails()
        newChild.link = '\'/nav' + strData + '\''
        newChild.name = strData
        baseRoot.child.append(newChild)

def processLising():
    replacement = []

    for r1 in allListing:
        replacement.append('<a href=' + '\'/nav' + r1 + '\'>' + r1 + '</a>')
        checkAndAdd(r1)


    data = template.replace('_BLOCK_TO_REPLACE_', '\n'.join(replacement))
    with open(currPath + '\\sitemap.html', "w+") as file:
        file.write(data)
    file.close()


getFilesOfDirs(navPath)
processLising()
print(baseRoot)
