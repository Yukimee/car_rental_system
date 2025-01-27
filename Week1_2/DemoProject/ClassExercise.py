class Color():
    #pass #blank class
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

def display_color(color: Color):
    print(f"Color: {color.red}, {color.green}, {color.blue}")


color = Color(red = 223, green = 122, blue =121)


display_color(color)
