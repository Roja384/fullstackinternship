#Animal sound system
from abc import ABC,abstractmethod 
class animal(ABC):
    @abstractmethod
    def sound():
        print("animal sound")
    def sleep(self):
        print("animal sleeps")
class dog(animal):
    def sound(self):
        print("bark")
class cat(animal):
    def sound(self):
        print("meow")
class cow(animal):
    def sound(self):
        print("moo")
c=cow()
c.sound()
c.sleep()

