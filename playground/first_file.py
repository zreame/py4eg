fname = input ('enter file name: ')

try :
    fhand = open(fname)
except :
    print ('file does not exist, quitting program now...')
    quit()

count = 0
for line in fhand :
    count = count + 1

print('num of lines: ', count)

fhand.seek(0)

print(fhand.read())












