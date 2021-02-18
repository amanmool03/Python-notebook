# # defining a class in python

class Student:
    def __init__(self, name, sclass, roll):
        # initialize your object variable
        self.name = name
        self.sclass = sclass
        self.roll = roll

    def get_name(self):
        return self.name

    def get_sclass(self):
        return self.sclass


std = Student('Ram', 10, 5)
# print(std.name, std.sclass, std.roll, std.get_name(), std.get_sclass())


class Teacher:
    def __init__(self, name, stds):
        # [('name':"Ram" ,"Sclass":10,"roll":5 )
        # ('name':"Ram" ,"Sclass":9,"roll":1 )
        # ]
        self.name = name
        students = []
        for std in stds:
            std_obj = Student(
                std['name'],
                std['sclass'],
                std['roll']
            )

            students.append(std_obj)
        self.stds = students

    def get_std_name(self):
        return [std.name for std in self.stds]

    def get_std_sclass(self):
        return [std.sclass for std in self.stds]


teacher = Teacher('xyz', [
    {"name": "Ram", "sclass": 10, "roll": 5},
    {"name": "shyam", "sclass": 9, "roll": 5}
])

print(teacher.get_std_name())
print(teacher.get_std_sclass())
# result = []
# for std in teacher.stds:
#     result.append(std.name)
# result = [std.name for std in teacher.stds]
# print(result)


class Product:
    def __init__(self, price, name, code, category):
        self.name = name
        self.price = price
        self.code = code
        self.category = category

    def price_level(self):
        if self.price > 1000:
            return "High"
        elif self.price > 100:
            return "Medium"
        else:
            return "Low"


# pycon
# real python
product = Product(2000, "pizza", "AB123", "Food")
print(product.price_level())
