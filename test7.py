##myl = [{'Release Year': '2007', 'Format': 'Blu-Ray', 'Stars':'Kate Higl, Paul Rudd, Leslie Mann', 'Title': 'Knocked Up'}]
##while myl:
##    z = myl.pop(0)
##    print z
def test_print():
    z = [1,2,3,4]
    while z:
        x = z.pop(0)
        print "x now is %s" % x
        print "z now is %s" % z


    z = [{1:2}, {3:4},]
    print "new z now is %s" % z
    while z:
        x = z.pop(0)
        print "x now is %s" % x
        print "z now is %s" % z

def main():
    test_print()

if __name__ == "__main__":
    main()
