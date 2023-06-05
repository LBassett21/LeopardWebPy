import kivy
from kivy.app import App
from kivy.uix.label import Label
import sqlite3

# creates a sql database called courses.db on the local dir
connection = sqlite3.connect("courses.db")

class leopardWeb(App):
    def build(self):
        return Label(text= "La website")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    leopardWeb().run()

# Testing of the gitbot