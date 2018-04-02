# ex 1
def get_output(inp):
    output=[]
    current_term=""
    for item in inp:
        if item.startswith("New:"):
            if current_term != "":
                output.append(current_term)
            current_term=item
        else:
            current_term = current_term + " " + item

    output.append(current_term)
    return output

# ex 2
def getDate(datestr):
    import re
    from time import strptime

    datestr = re.sub(r'\W+', "", datestr)  # to replace spl chars
    dd = ""
    mm = ""
    yyyy = ""
    mm = str(strptime(re.sub(r'\d+', "", datestr), '%b').tm_mon).zfill(2)  # to work mon like jan by removing numeric chars
    for token in re.findall(r'\d+', datestr):  # iterating over numeric tokens
        if int(token) <= 12:
            if mm != "":
                mm = token
        elif int(token) < 31:
            dd = token
        else:
            yyyy = token

    if dd == "":
        dd = "99"
    if mm == "":
        mm = "99"
    if yyyy == "":
        yyyy = "9999"
    return dd + "-" + mm + "-" + yyyy

def ex_1_style2(input_arr):
    outlist = [s.replace("New", "$New") for s in input_arr if s.startswith("New") or len(s) > 0]
    outlist = [s.strip() for s in (" ".join(outlist)).split("$")[1:]]
    print("\n**** String output - style 2 ********\n")
    print(outlist)




# using recursion * not working
def ex_1_style3(stritem,output,item):
    itm=''.join(stritem[:1])
    if stritem[:1]==[]:
        return output
    elif itm.startswith("New:"):
        item=item+1
        output.append(itm)
        ex_1_style3(stritem[1:], output,item)
    else:
        output[item]=output[item]+" "+itm
        ex_1_style3(stritem[1:],output,item)



def main():
    input_arr = [
        "New: Hello",
        "How are",
        "you",
        "New: I am",
        "fine"
    ]

    print(get_output(input_arr))


    print(getDate("2013Jan20"))
    print(getDate("2013Jan"))
    print(getDate("20Jan2013"))
    print(getDate("2013/Jan/20"))

    ex_1_style2(input_arr)

    #using recursion
    temp = []
    print(ex_1_style3(input_arr, temp, -1))
    print(temp)


if __name__ == '__main__':main()
