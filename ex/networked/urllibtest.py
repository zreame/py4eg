import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand :
    print(line.decode().strip())
    # remove spaces
    print(line.decode().strip().replace(' ',''))
    # removes spaces, tabs, newlines
    print(" ".join(line.decode().split()))
