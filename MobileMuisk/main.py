from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from math import sqrt
from kivy import Config
Config.set('graphics', 'multisamples', '0')

Builder.load_file('design.kv')
     
class RootWidget(ScreenManager):
    pass

class CalculateScreen(Screen):
    def get_number(self,cateto):
        catetoAdy = float(cateto)
        catetoOpuesto = float(sqrt((catetoAdy * catetoAdy) - 0.0144 ))
        if catetoAdy < 0:
           self.ids.result.text="Digito Incorrecto" 
        else:
           catetoOpuesto = str(catetoOpuesto)
           self.ids.result.text=catetoOpuesto  
    
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()