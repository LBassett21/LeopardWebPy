import kivy
from kivy.app import App
from kivy.uix.label import Label



class leopardWeb(App):
    def build(self):
        return Label(text= "La website")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    leopardWeb().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
