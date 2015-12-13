from kivy.uix.button import Button
from kivy.utils import get_random_color


class Menu_Button(Button):
    def __init__(self, **kwargs):
        super(Menu_Button, self).__init__(**kwargs)
        self.background_color = get_random_color()
        if 'screenmanager' and 'screen' in kwargs:
            self.sm = kwargs['screenmanager']
            self.screen = kwargs['screen']


    def on_press(self):
        super(Menu_Button, self).on_press()
        try:
            self.sm.current = self.screen
        except:
            pass