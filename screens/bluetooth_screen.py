from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from buttons.menu_button import Menu_Button
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton, ListView
from kivy.adapters.listadapter import ListAdapter
from kivy.clock import Clock
import bluet
from threading import Thread
import Queue

queue = Queue.Queue()

class DataItem(object):
    def __init__(self, mac_addr, name):
        self.mac_addr = mac_addr
        self.name = name

class Bluetooth_Screen(Screen):
    def __init__(self, color=(0, 0, 0), **kwargs):
        super(Bluetooth_Screen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(color[0] / 256., color[1] / 256., color[2] / 256.)
            self.rect = Rectangle(size=self.size)

        self.name_dict = {}
        args_converter = lambda row_index, data_item: {'text': data_item.name, 'size_hint_y': None, 'height': 25}
        self.adapter = ListAdapter(data=[], args_converter=args_converter, cls=ListItemButton, selection_mode='single')
        self.adapter.bind(on_selection_change=self.item_selected)
        self.discovered_list = ListView(size_hint=(.5, .5), adapter=self.adapter)
        self.add_widget(self.discovered_list)

        self.info_label = Label(size_hint=(.5, None), height=30)
        self.add_widget(self.info_label)

        self.bind(size=self.update)

    def update(self, *args):
        self.rect.size = self.size
        self.discovered_list.pos_hint = {'center_x': .5, 'center_y': .5}
        self.info_label.pos_hint = {'center_y': .8, 'center_x': .5}
    def builder(self):
        self.add_widget(Menu_Button(size_hint=[.1, .1], text='Go Back', screenmanager=self.manager, screen='menu'))
        self.discover_button = Menu_Button(size_hint=[.1, .1], pos_hint={'right': 1}, text='Discover')
        self.add_widget(self.discover_button)
        self.discover_button.bind(on_press=self.start_discover)

    def start_discover(self, *args):
        Clock.schedule_interval(self.discover, .5)


    def discover(self, *args):

        if not self.discover_button.disabled:
            self.discover_button.disabled = True
            self.info_label.text = "Discovering devices..."
            discover_thread = Thread(target=bluet.discover_thread, args=(queue,))
            discover_thread.start()

        items = []
        if not queue.empty():
            discovered = queue.get()
            for x in discovered:
                items.append(DataItem(x, discovered[x]))
            self.adapter.data = items
            self.discover_button.disabled = False
            self.info_label.text = "Select device"
            Clock.unschedule(self.discover)


    def item_selected(self, *args):
        text = 'Device selected MAC: ' + args[0].data[0].mac_addr
        self.info_label.text = text


