#print ('\n')
#import readline
#with open ('movies.txt', 'r') as f:
#    read_data = f.readline(4)
#    print read_data
#f.closed
#dict_from_file = []
#f = open ('movies.txt', 'r')
#for line in iter(f):
#    print line
#f.close()
dicts_from_file = []
with open('movies.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval(line))
print dicts_from_file
