#dict_from_file = []
#f = open ('moviessimple.txt', 'r')
#for line in iter(f):
#    #print line
#    dict_from_file.append(eval(line))
#f.close()
# Save a dictionary into a pickle file.
import pickle

#favorite_color = { "lion": "yellow", "kitty": "red" }

#pickle.dump( favorite_color, open( "save.p", "wb" ) )
favorite_color = pickle.load( open( "save.p", "rb" ) )
print favorite_color
smm = pickle.load( open("moviessimple.txt", "rb") )

