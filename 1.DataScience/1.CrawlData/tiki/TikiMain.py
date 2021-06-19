from TikiTarget import TikiTarget



TARGET_FILE = 'target_list.txt'
targetFile = open(TARGET_FILE,'r',encoding='utf8')
lines = targetFile.readlines()
targetFile.close()

for line in lines:
    newLine = line.strip()
    newTarget = TikiTarget(newLine,newLine)
    print(newTarget.info())
    # print(line.strip())
