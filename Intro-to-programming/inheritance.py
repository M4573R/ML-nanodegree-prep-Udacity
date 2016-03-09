


class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color




class Child(Parent):

    def __init__(self,last_name,eye_color,number_of_toys):
        print "Child Constructor Called"
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys=(number_of_toys)



Ryli = Child("Cirus","blue",34)
print Ryli.last_name
print Ryli.number_of_toys
