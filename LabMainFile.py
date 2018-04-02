import datetime
from functools import reduce

x = 10 # global var

def main():
    #x = 1 #local var
    global x
    print("hello")
    #print(x)
    #print(findMyAge())
    #-------findMyAge()

    #print(map(lambda w: len(w), 'It is raining cats and dogs'.split()))
    #map(<function>, <sequence/list>)
    #TODO: map() & lambda
    #---------lamdatest()
    test()

def findMyAge():
    print(datetime.date.today())
    dob = input("Enter your year of birth : ")
    currdate = datetime.datetime.now().year #datetime.date.today()
    age = currdate - int(dob)
    print(age)
    #return age

def lamdatest():
    sentence = 'It is raining cats and dogs'
    words = sentence.split()
    print(words)
    lengths = map(lambda word: len(word), words)
    print(lengths)


def test():
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, items))
    print(squared)

    print(list(map(lambda x:x+1,[1,2])))

    print("\nreduce ::: ")
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
    print("\nmap ::: ")
    print(list(map(lambda x,y:x+y, [1,2,3,4,],[2,3,4,2])))

if __name__ == '__main__':main()
