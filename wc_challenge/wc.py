import sys

arr = sys.argv
fl= sys.argv[-1]
readFromFile =True

if fl[0]=="-" or len(arr)==1:
    fl = ""
    contents = sys.stdin.read()
    readFromFile = False
else:
    with open(fl,'r') as file1:
        contents=file1.read()

try:
    lines = ((len(contents.split('\n')))-1)
    words = (len(contents.split()))
    bytes= (len(contents.encode('utf-8')))
    chars= (len(contents))
    if '-l' in arr:
        print(lines)
    if '-w' in arr:
        print(words)
    if '-c' in arr:
        print(bytes)
    if '-m' in arr:
        print(chars)
    if len(arr)==1 and readFromFile == False: 
        print(lines, words, bytes, fl)
    if len(arr)==2 and readFromFile == True:
        print(lines, words, bytes, fl)
except FileNotFoundError:
    print(fl, ": No such file or directory")


