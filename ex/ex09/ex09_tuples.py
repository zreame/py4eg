fname = input('Enter file name: ')

# here clown.txt is short test file, so no need input when testing
if len(fname) < 1 : 
    fname = 'clown.txt'

# impt, handling bad file names
try:
    fhand = open(fname)
except:
    print ('filename does not exist')
    quit()

di = {}
count = 0

for line in fhand :
    # always do rstrip() to remove \n in file lines
    wds = line.rstrip().split()
    for w in wds:
        # pro method for .get() to inset into dict as key, value pairs
        di[w] = di.get(w,0) + 1
        count = count + 1
        # print(w)

# freqmax = None
# wordmax = None

# # previous method .items() to loop a dictionary into the key value pairs
# for word, freq in di.items() :
#     if wordmax is None or freq > freqmax :
#         wordmax = word
#         freqmax = freq

# ---""""---------

# sorted function, comparing alphabetical order, not really useful:

# print(sorted(di.items()))

# print('test', di.items()[0])

# method 2 List Comprehension, more elegant method
# sorted() to find highest freq in dict (replacing above)
# reverse = True for descending order

list_tuple = sorted( [ (v,k) for k,v in di.items() ], reverse = True )

print('highest word is:', list_tuple[0][1], 'with freq:', list_tuple[0][0] )
print('total words:', count)
print('total unique words:', len(di))