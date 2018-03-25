'''
Please don't bother about the computation happening here. its deliberately twisted to explore inheritance features in python.
'''

class GrandParent:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print("grandparent.adding...(a+b)=", self.a+self.b)
        return self.a+self.b

class Parent(GrandParent):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mul(self):
        c = super().add()  #call parent method
        print("parent.multiplying...(a+b)*(a*b)=", self.a*self.b*c)
        return self.a*self.b*c

class Child(Parent, GrandParent):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print("child.showing...(a+b)+(a+b)+(a*b)=", self.add() + self.mul())
        return self.add() + self.mul()

def main():

    vars = (1,2) # set a,b

    child = Child(*vars) # pass non key worded args

    print("\na+b = ",child.add()) # call grandparent class function **working
    print("\n(a+b)*(a*b) = ", child.mul())  # call parent class function
    child.show() # call grandchild class function


if __name__ == '__main__':main()
