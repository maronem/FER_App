import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGridLayout(Widget):
    
    def press(self, instance):
        #self.greeting.text = f"Hi {self.username.text}!"
        self.welcome_msg.text = f"Hi {self.username.text}! Welcome back to KivyApp"

        # Clear input boxes
        self.username.text = ""
        self.password.text = ""

    def center_text(self, text_input, *args):
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached)
        text_input.padding_x = (text_input.width - text_width)/2

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()