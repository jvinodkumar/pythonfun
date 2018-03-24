import datetime

x = 10 # global var

def main():
    #x = 1 #local var
    global x
    print("hello")
    #print(x)
    #print(findMyAge())
    #findMyAge()

    #print(map(lambda w: len(w), 'It is raining cats and dogs'.split()))
    #map(<function>, <sequence/list>)
    #TODO: map() & lambda
    lamdatest()

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





if __name__ == '__main__':main()
