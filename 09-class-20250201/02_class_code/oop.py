
class Student:  # this
    def __init__(self, obj_name, obj_age=20):
        self.name = obj_name
        self.age = obj_age
        # self.roll_no = 0
    

    def complete_assignment(self):
        print("Printing self", self)
        print(self.name + " has completed the assignment")

#================================================================


s1 = Student("John")

print(s1.name)
# print(s1.roll_no)

s1.complete_assignment()
print("Printing s1", s1)


s2 = Student("Alice", 29)

print(s2.name)
# s2.complete_assignment()


#initialize the object


# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(type(num))

# num.append(11)