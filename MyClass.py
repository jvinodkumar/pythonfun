
var = "test"
class MyClass:

    var = "jayakumar"
    #constructor
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def getName(self):
        return self.name+self.var
    def getAge(self):
        return self.age


def test_non_keyworded_var_args_call(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

def test_keyworded_var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

def main():
    #c = MyClass("vinod",28)
    c=MyClass(name="vinod",age=29)
    print(c.getName(),c.getAge())
    nameargs=("rajesh")

    c=MyClass(nameargs,"39")
    print(c.getName(), c.getAge())

    mynames = {"name":"robert","age":34}
    c = MyClass(**mynames)
    print(c.getName(), c.getAge())

    # test *args (non key worded arguments)
    args = ("two", 3)
    test_non_keyworded_var_args_call(1, *args)

    # test **kwargs (keyworded arguments)
    kwargs = {"arg3": 3, "arg2": "two"}
    test_keyworded_var_args_call(1, **kwargs)


if __name__ == '__main__':main()
