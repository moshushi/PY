# -*- coding: cp1251 -*-

def instar():
    li=[]
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
