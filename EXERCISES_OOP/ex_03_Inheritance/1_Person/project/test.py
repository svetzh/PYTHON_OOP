<<<<<<< HEAD
from project.person import Person

from project.child import Child

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
=======
from project.person import Person

from project.child import Child

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
>>>>>>> 276765b8e88ecb03013f4fe22c25ddcd3699ae0d
print(child.__class__.__bases__[0].__name__)