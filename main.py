import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# 
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

fig,ax = plt.subplots()

canvas= fig.canvas

import numpy as np

class Home(ScreenManager):
    def __self__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
    
    def generate_graph(self):
       self.fn = self.ids.fn
       self.fist_value_of_x = self.ids.first_value
       self.final_value_of_x = self.ids.final_value
       self.number_of_domain = self.ids.number_of_domain

       first_value = int(self.fist_value_of_x.text)
       final_value = int(self.final_value_of_x.text)
       number_of_domain = int(self.number_of_domain.text)

       x = np.linspace(first_value, final_value, number_of_domain)
       y = eval(self.fn.text)

       plt.plot(x,y)
       plt.grid()

       canvas= FigureCanvasKivyAgg(plt.gcf())
       self.graph = self.ids.graph
       self.nav = NavigationToolbar2Kivy(canvas)

       self.graph.add_widget(self.nav.actionbar)
       self.graph.add_widget(canvas)

class MainApp(MDApp):
    def build(self):
        Builder.load_file('main.kv')
        return Home()
    
MainApp().run()