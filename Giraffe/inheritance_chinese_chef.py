from inheritance_chef import  Chef


class ChineseChef(Chef):

    # override the make_special_dish from Chef
    def make_special_dish(self):
        print("The Chef makes Orange Chicken")

    def make_fried_rice(self):
        print("The Chef makes fried rice")
