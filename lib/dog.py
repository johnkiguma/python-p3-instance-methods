#Add an instance method sit() to your Dog class that will print "The dog is sitting."

#!/usr/bin/env python3

class Dog:
    
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

fido = Dog()
fido.sit()

snoopy = Dog()
snoopy.bark()

fido.sit


