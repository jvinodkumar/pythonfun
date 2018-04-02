import urllib.request, json
import mylab
import datetime
import dateutil


def apicall():
    url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22nome%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    data = urllib.request.urlopen(url).read()
    #print(data)

    jsondata = json.loads(data.decode("utf-8"))
    print(jsondata["query"]["results"]["channel"]["location"])

#def mymap():

def ex1():
    input_arr = [
        "New: Hello",
        "How are",
        "you",
        "New: I am",
        "fine"
    ]

    outputLine=""
    output=[]
    i=0
    newFlag=False
    for item in input_arr:
        i=i+1
        if item.startswith("New"): #and outputLine != "":
            #output.append(outputLine)
            newFlag=True
            #outputLine=""
            outputLine = item
        else:
            outputLine = outputLine + " "+item

        if item.startswith("New")==False and newFlag==True: #i==len(input_arr):
            output.append(outputLine)
            outputLine=""
            newFlag=False

    print(output)

# working piece here down ex11
def ex11():
    input_arr = [
        "New: Hello",
        "How are",
        "you",
        "New: I am",
        "fine"
    ]

    outputLine = ""
    output = []
    i = 0
    for item in input_arr:
        i = i + 1
        if item.startswith("New") and outputLine != "":
            output.append(outputLine)
            outputLine = item
        else:
            outputLine = outputLine + " " + item

        if i==len(input_arr):
            output.append(outputLine)

    print(output)

#    for iter in input_arr.__iter__()
 #       iter.
  #  print(str(input_arr.__iter__().__next__())

def collabnotebook():
    print(list(filter(lambda line: line.startswith("New"), ["New: Hello",
                                                            "How are",
                                                            "you",
                                                            "New: I am",
                                                            "fine"])))

    input_arr = [
        "New: Hello",
        "How are",
        "you",
        "New: I am",
        "fine"
    ]
    print(list(filter(lambda line: line.startswith("New"), input_arr)))
    # print(list(map(lambda)))

    # if lambda x:x.startswith("New"),list(filter(lambda line:line.startswith("New"),input_arr)) == True:
    #   print(x)

    output = []
    outlist = []
    # special_squares = [ x**2 for x in range(10) if x**2 > 5 and x**2 < 50 ]
    # [output.append(line) for line in range(len(input_arr)) if filter(lambda elem:len(elem)>0,input_arr) == True ]
    # print(output)
    newline = ""
    lastelem = ""
    newlinecount = 0
    for elem in input_arr:
        if elem.startswith("New"):
            newline = newline + elem
            output.append(newline)
        else:
            newline = newline + " " + elem

    lastelem = elem
    output.append(lastelem)
    print("output\n-----")
    print(output)


'''2013Jan20 - ----> 20 - 01 - 2013
    2013Jan - ----> 99 - 01 - 2013
    20Jan2013 - ----> 20 - 01 - 2013
    2013 / Jan / 20 - ----> 20 - 01 - 2013
'''
# input YYYYMMMDD or YYYYMMM or DDMMYYYY or YYYY / MMM / DD

# output format MM-DD-YYYY
def convertDates(inputDate):

    #print(len(inputDate))
    #print(inputDate[4])
    #print(inputDate[4].isalpha())
    #2013Jan02
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    month=""
    date=""
    year=""

    if inputDate.find("/")>-1:
      #  print("Date format is YYYY / MM / DD")
        year=inputDate[0:4]
        month=inputDate[8:9]
        day=inputDate[-2:]
     #   print(year+month+year)

    elif len(inputDate)<8:
        print("Date format is YYYYMMM")
    elif inputDate[4].isalpha()==True and len(inputDate)==9:
        print("Date format is YYYYMMMDD")
        print(inputDate.split("Jan".capitalize())[0], inputDate.split("Jan".capitalize())[1], m)
    elif len(inputDate)==8:
        print("Date format is DDMMYYYY")
    else:
        print("Could not detect the format")

    res = "2017Jan18".split("Jan")

    #print(list(filter(lambda x:"2017Jan18".split(x),months)))

    for m in months:
         #m="Jan"
         dylist = "2017Jan20".split("Jan".capitalize())
         #print(m,dylist[0])

         print("2017Jan20".split("Jan".capitalize())[0],"2017Jan20".split("Jan".capitalize())[1],m)

         #filter(lambda x:"2017Jan20".split(x.capitalize()),months)
         print("2017Mar20".count(m))
         #print(dylist[0])


         #df['Jan'] = df['01'].apply(lambda x: calendar.month_name[x])

    #print(res)

   # day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

   #  MM=""
   # monTomm = dict(01="Jan",Feb="02",Mar="03",Apr="04")



#    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
#    for mon in months:
#        if inputDate.find(mon.title()) :
#            print("Month is : ",mon.title())





    #print(inputDate.find())

    #for char in inputDate:
     #   if char.isalpha()==True and inputDate.index(char)==4:
            #Year is in YYYY formnat
      #  if char.isalpha()==True  # MMMDD detected
       # print(char, char.isalpha(), inputDate.index(char))
        #print(inputDate.index(char))



def main():
    #ex11()
    #convertDates("2018 / 12 / 27")
    #print(mylab.hello())
    #convertDates("02081980")
    #convertDates("02081980")
    #convertDates("02081980")

    #mydate = datetime.datetime.now()
    #print(mydate.strftime("%b"))
    datelist = ["2017Jan12","27012018","02-Jan-2018"]
    #for x in datelist:
    #    print(parser.parse(x))

    newdate = datetime.datetime.strptime(datelist[0], '%b %d %Y %I:%M%p').strftime('%Y/%m/%d %I:%M%p')
    print(newdate)

if __name__ == '__main__':main()
