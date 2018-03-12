import os
import glob
import binascii


if not os.path.exists("raps"):
    os.makedirs("raps")

entries_c00 = []
entries_psn = []

entries = open("database").read().split("\n")


for entry in entries:
    if entry.split(";")[2] == "C00":
        entries_c00.append(entry)
f = open("c00.txt", "w")
for entry in entries_c00:
    entry = entry.split(";")[0:4]
    f.write(entry[0] + "\n" + entry[1] + "\n" + entry[2] + "\n" + entry[3] + "\n")
f.close()



"""
entries = glob.glob(".\data\*.txt")

print len(entries)

for entry in entries:
    with open(entry, "r") as f:
        try:
            s = f.read().split(";")[3]
            if s == "JP" or s == "HK":
                f.close()
        except:
            print "Ooops!!!"        



for i in title_id:
    print count
    print i
    count = count + 1
"""

"""
for i in range(len(data)-1):
    if ".rap" in data[i] and " .rap" not in data[i]:
        print data[i]
        print data[i+1]
        with open(".\\raps\\" + data[i], "w") as rap:
            rap.write(binascii.unhexlify(data[i+1]))
"""