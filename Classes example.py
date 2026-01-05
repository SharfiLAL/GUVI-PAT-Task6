class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):  # Constructor method
        self.name = name  # Instance attribute
        self.age = age

    def speak(self, sound):
        return f"{self.name} says {sound}"

buddy = Dog("Buddy", 5)
print(buddy.speak("Woof"))