#qpy:kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from screens.menu_screen import Menu_Screen
from screens.bluetooth_screen import Bluetooth_Screen


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)


class MainApp(App):
    def build(self):
        root = Manager(transition=FadeTransition())
        menu = Menu_Screen(name='menu', color=(140, 200, 123))
        bluetooth = Bluetooth_Screen(name='bluetooth', color=[120, 60, 60])
        root.add_widget(menu)
        root.add_widget(bluetooth)


        #We have to call builder after the creation of the screen
        #and assign it to root,  when it gets a ScreenManager.
        menu.builder()
        bluetooth.builder()

        return root


if __name__ == '__main__':
    MainApp().run()
