import os

def getDirSize(path, sizeLimit):
    curSize = 0
    curList = []

    try:
        for pathElem in os.listdir(path):
            subPath = path + '\\' + pathElem
            subTree = []
            subSize = 0
            if os.path.isdir(subPath):
                subDirResult = getDirSize(subPath, sizeLimit)
                subSize = subDirResult[0]
                subTree = subDirResult[1]
            else:
                subSize = os.path.getsize(subPath)

            curSize += subSize
            if subSize >= sizeLimit:
                if len(curList) == 0:
                    curList += [(subSize, subPath, subTree)]
                else:
                    for i in range(len(curList)):
                        if subSize >= curList[i][0]:
                            curList.insert(i, (subSize, subPath, subTree))
                            break
    except:
        pass

    return (curSize, curList)

def printTree(outputFile, tree, level):
    for elem in tree:
        print('-'*level, int(round(elem[0]/1024/1024,0)), elem[1], file=outputFile)
        if elem[2]:
            printTree(outputFile, elem[2], level+1)


#print(ctypes.windll.shell32.IsUserAnAdmin())
initDir = 'C:\\'
sizeLimit = 1024 * 1024 * 1024

outputFile = open('diskStat.txt','w')
res = getDirSize(initDir, sizeLimit)
print(int(round(res[0]/1024/1024,0)),initDir, file=outputFile)

printTree(outputFile, res[1],0)
