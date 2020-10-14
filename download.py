import urllib.request
import bz2  # bz2
from pyunpack import Archive  # 7z

f = open("download_links", "r")
f1 = f.readlines()
a = 1

for x in f1:
    v = "file" + str(a)
    print(x)

    # downloading the files and putting them to "zipped" folder
    filedata = urllib.request.urlopen(x)
    datatowrite = filedata.read()
    with open('zipped/' + v, 'wb') as f:
        f.write(datatowrite)

    # bz2 extension
    if ("bz2" in x):
        zipfile = bz2.BZ2File('zipped/' + v)  # open the file
        data = zipfile.read()  # get the decompressed data
        open('unzipped/' + v, 'wb').write(data)  # write a uncompressed file

    print(a)
    a += 1
