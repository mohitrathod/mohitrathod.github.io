from os import listdir, makedirs
from os.path import isfile, join, dirname
import re

mypath = "C:/Users/rathomoh/temp/site"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
dirs = [f for f in listdir(mypath) if not isfile(join(mypath, f))]

print(files)
print(dirs)


redirectPageTemplate = open(mypath + '/' + "templateSitemap.html", 'r').read()

def processFiles(currentPath , inputFiles):

    for file in inputFiles:
        with open(currentPath + '/' + file, 'r') as content_file:
            if not content_file.name.endswith('html'):
                continue
            try:
                content = content_file.read()
                pattern = 'href=[\'"]?([^\'" >]+)'
                ngUrlMatches = re.findall(pattern, content)

                for ngUrl in ngUrlMatches:
                    print(ngUrl)
                    if ngUrl.startswith('http') or '.' in  ngUrl:
                        continue
                    outTemplate = redirectPageTemplate % (ngUrl, ngUrl)
                    # print(outTemplate)
                    print("--------------------------------")
                    fileName = mypath + '/nav/' + ngUrl.replace('#', '/').replace('//','/') + '.html'
                    makedirs(dirname(fileName), exist_ok=True)
                    with open(fileName, "w") as file:
                        file.write(outTemplate)
                        file.close()

            except Exception as e:
                print(e)


def getFilesOfDirs(currentDir, inputDirs):

    for dir in inputDirs:
        if dir == 'nav':
            continue
        files = [f for f in listdir(currentDir + '/' + dir) if isfile(join(currentDir + '/' + dir, f))]
        processFiles(currentDir + '/' + dir, files)
        # getFilesOfDirs()

processFiles(mypath, files)

getFilesOfDirs(mypath, dirs)
