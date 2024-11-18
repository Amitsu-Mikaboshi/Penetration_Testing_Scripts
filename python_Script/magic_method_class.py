# first of all intro. Here we will learn some advance topic which is magic methode. Maybe we are familiar with it but never thought how its work and what
# is it. If anyone familiar with Pandas and Matlab module they will often use import matlab as mb!! Well then what does it mean and how its work?
# first of all that module is build with OOP rather than structural programming . and there it contain a magic method called __enter__ , __exit__
# lets dive deep into it

class fooHacked():
    def __init__(self,input="no-One"):
        self.input = input

    def __str__(self):
        return f'My object string formate must be like that!! By the way HIII {self.input}' # this will tell how to interupt with the function string
    
#time to interact with the class by creating object
normal_object = fooHacked(input='silly Meow')
print(normal_object) #generally you can not print the raw object because its a data not string. but as a Developer you can specify how your object will
# show if user wants to know what its about. So its recommended to give manual in string section . In short, it will represent your object class as a string



#another valuable magic method that gives you the wing to interrupt with it; using with
class testing_with():
    age = 10
    def __enter__(self): # enter and exit magic method will allow you to interact this class object as with 
        print('This is the starting...') 
        return self #must be return something. because we are now using enter block . So its important that the enter block is responsible for data input and output
    def __exit__(self, type, value, traceback):
        print('.....This is the ending of the snippet')

#interrupt the class using object
with testing_with() as test:
    print(f'using the testing_with and check if age: {test.age} is working')
# this is just like we are using open module in python : with open('file_path','w') as wr; wr.write('something')
# now compare and you will have your answer,  how those functions are worked.