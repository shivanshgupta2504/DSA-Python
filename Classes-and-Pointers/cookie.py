class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):  # getter method
        return self.color
    
    def set_color(self, color):
        self.color = color
    

cookie1 = Cookie('red')
cookie2 = Cookie('green')

print(f"Cookie 1 color: {cookie1.get_color()}")
print(f"Cookie 2 color: {cookie2.get_color()}")

cookie1.set_color('blue')

print(f"\nUpdated Cookie 1 color: {cookie1.get_color()}")
print(f"Cookie 2 color: {cookie2.get_color()}")