
def main():

    print("\nEnter 'end' to exit")

    while True:
        val = input("\nEnter contact name : ")
        if val == "end":
            break
        else:
            addToFile(val)

    readFile()

def addToFile(line):
    out = open("contact.txt","a")
    out.write("\n"+line)
    out.close()

def readFile():
    filestr = open("contact.txt","r")
    for line in filestr:
        print(line)
    filestr.close()

def testWriteFile():
    try:
        out = open("test.txt","w")
        out.write("this is first file")
        out.close()
    except IOError:
        print("error creating file")

def testReadFile():
    try:
        readfile = open("test.txt","r")
        for line in readfile:
            print(line)
        readfile.close()
    except IOError:
            print("exception while reading file")

if __name__ == '__main__':main()
