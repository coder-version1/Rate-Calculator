# create a GUI -
#     Input screen GUI -
#         1) create a form to get the user input - as to what he/she wants to ship
#         2) another field that takes in the qty
#         3) a 'calculate' button
#
#     Output screen GUI
#         1) a label/ just a window that displays 'your shipping cost would be '
#
# Create the backend -
#     1) Once the user clicks the calculate button, the program must take the data from the databse csv file in the computer
#     2) use then information and calculate the shipping cost
#     3) use Fedex, UPS, USPS APIs for calculation


import kivy
import pandas

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class layout(GridLayout):
    def __init__(self, **kwargs):
        super(layout, self).__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text="Rate Calculator - Please enter qty for each", font_size=25))

        self.inside = GridLayout()
        self.inside.cols = 2

        source = pandas.read_csv('project_database.csv')
        things = source['Item'].iloc[:]

        quantity = []

        for rows in things:
            self.inside.add_widget(Label(text=(str(rows))))
            self.qty = TextInput(multiline=False)
            quantity.append(self.qty.text)
            self.inside.add_widget(self.qty)


        self.add_widget(self.inside)
        self.calculate = Button(text='calculate', font_size=25)
        # self.calculate.bind(on_press=self.pressed, quantity)
        self.add_widget(self.calculate)

    def pressed(self, instance, quantity):
        print(quantity)



class MyApp(App):
    def build(self):
        return layout()


if __name__ == "__main__":
    MyApp().run()
