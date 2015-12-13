from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from buttons.menu_button import Menu_Button
from kivy.graphics import Color, Rectangle
from kivy.app import App


class Menu_Screen(Screen):
    def __init__(self, color=(0, 0, 0), **kwargs):
        super(Menu_Screen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(color[0] / 256., color[1] / 256., color[2] / 256.)
            self.rect = Rectangle(size=self.size)

        self.bind(size=self._update)



    def _update(self, *args):
        self.rect.size = self.size

    def builder(self, *args):

        # Menu Layout and Buttons
        buttons_grid = GridLayout(cols=1, size_hint=[0.3, 0.1],
                                  pos_hint={'center_x': self.center_x, 'center_y': self.center_y})

        button_1 = Menu_Button(text='Bluetooth', screenmanager=self.manager, screen='bluetooth')
        buttons_grid.add_widget(button_1)

        button_2 = Menu_Button(text='Exit')
        buttons_grid.add_widget(button_2)
        button_2.bind(on_press=self.exitApp)

        self.add_widget(buttons_grid)

    def exitApp(self, *args):
        App.get_running_app().stop()
