from os import listdir
from os.path import isfile, join

mypath = "./craftsdb"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlynames = [f.split(".png")[0] for f in onlyfiles]
onlynames = [f.split(".jpg")[0] for f in onlynames]
onlynames = [f.split(".webp")[0] for f in onlynames]

for fi in range(0,len(onlyfiles)):
    path = mypath + "/" + onlyfiles[fi]
    updateStatement = "UPDATE ARTS SET img = LOAD_FILE('%s') WHERE Name='%s';" % (path,onlynames[fi])
    print(updateStatement)