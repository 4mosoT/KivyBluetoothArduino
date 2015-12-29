from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from buttons.menu_button import Menu_Button
from kivy.uix.label import Label
import bluet

class Bluetooth_Screen(Screen):
    def __init__(self, color=(0, 0, 0), **kwargs):
        super(Bluetooth_Screen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(color[0] / 256., color[1] / 256., color[2] / 256.)
            self.rect = Rectangle(size=self.size)
        self.bind(size=self.update)

        self.blue_label = Label(text="Here should appear Bluetooth Device MAC")

        self.add_widget(self.blue_label)

    def update(self, *args):
        self.rect.size = self.size

    def builder(self):
        self.add_widget(Menu_Button(size_hint=[.1, .1], text='Go Back', screenmanager=self.manager, screen='menu'))
        discover_button = Menu_Button(size_hint=[.1, .1], pos_hint={'right': 1}, text='Discover')
        self.add_widget(discover_button)
        discover_button.bind(on_press=self.discover)

    def discover(self, *args):
        self.blue_label.text = "Searching for devices..."
        discovered = bluet.discover()
        self.blue_label.text = str(discovered)
        #TODO: Discover devices within paralell threading.
