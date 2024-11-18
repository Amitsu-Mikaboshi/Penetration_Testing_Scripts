class bakery:
    size = None
    weight_lb = None
    ready = False
    topping = None
    garnish = None

    def __init__(self,topping='No topping',garnish='No garnish',size=10,weight_lb=1):
        self.topping = topping
        self.garnish = garnish
        self.size = size
        self.weight_lb = weight_lb
    def baked_ready(self):
        self.ready = True
        return self.ready
    
#creating instance/object to interact with the created class
normal_cake = bakery() #this object will have default values
luxary_cake = bakery(size=50,weight_lb=20,topping='Chocolate Topping',garnish='Strawberry Garnish') #this object will have customized value

print(luxary_cake.size) #interacting with the class via object
luxary_cake.size = 10
print(luxary_cake.size) #we can even modify the class object. but it will only change in object not in the class. Class is the blueprint.And object is the 
#main thing we can modify



    