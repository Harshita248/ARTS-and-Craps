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


# Old code for creating sql script
'''
data = []
    with open('Arts.tsv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter='\t')
      print("Use `ArtsAndCraps`;")
      for row in spamreader:
          for r in range(0,len(row)):
              row[r] = row[r].replace('  ',' ')
              row[r] = row[r].replace('\'','\\\'')
              row[r] = row[r].replace('\"','\\\"')
          print("INSERT INTO Arts (Name, Img) VALUES (\"%s\",\"%s\");" % (row[0],0))
          materials = row[1].split("\n")
          for m in materials:
              if m != "" and m!=" ":
                print("INSERT INTO Material(Name,Material) VALUES (\"%s\",\"%s\");" % (row[0],m))
          steps = row[2].split("\n")
          stepcounter = 1
          for s in range(0,len(steps)):
            step = steps[s]
            if step != "" and step != " "
                print("INSERT INTO Instruction(Name,Instruction,StepNumber) VALUES (\"%s\",\"%s\",\"%s\");" % (row[0],step,s))
                stepcounter = stepcounter + 1
'''