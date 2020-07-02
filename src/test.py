class class1:
    def function(self):
        return 1


class class2:
    def function(self):
        return 2


# class class3(class1, class2):
#     pass

class class3(class2, class1):
    pass


print(class3().function())
