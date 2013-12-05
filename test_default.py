
# -*- coding: cp1251 -*-

def instar():
    #while st !=
    #i=raw_input("Please enter name [Jack]:" or "Jack"
    #res = raw_input('Folder [default] :')
    #res = res or 'default'
    li=[]
    #while n != '\r'
    while True:
        n = raw_input('Enter n or enter Enter to quit')
        if not n:
            break
        li.append(n)
        print li
    print ('Loop end')


def main():
    instar()

if __name__ == "__main__":
    main()
