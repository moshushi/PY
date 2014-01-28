#f = open ('movies.txt','r')
#print f.readline()
#print f.readline()
#print f.readline()
#for line in f:
#    print line
#print list(f)
with open ('movies.txt', 'r') as f:
    read_data = f.read()
    print read_data
f.closed
