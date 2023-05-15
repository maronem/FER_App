from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty


class FERApp(App):
    def build(self): # build returns root widget
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #add widgets to window

        #IMAGE  WIDGET
        self.window.add_widget(Image(source="fruit_img.png",))

        #LABEL WIDGETS
        self.greeting = Label(text="Hello from Kivy \n" + "Welcome to your daily journal!",
                              font_size = 18)
        self.window.add_widget(self.greeting)
        #name label widget
        self.greeting = Label(text="\n Hello, what is your name?")
        self.window.add_widget(self.greeting)
        #name text input widget
        self.user = TextInput(multiline=False) #width, height
        self.window.add_widget(self.user)
        #age label widget
        self.ask_age = Label(text="\n How old are you?")
        self.window.add_widget(self.ask_age)
        #age text input widget
        self.user_age = TextInput(multiline=False)
        self.window.add_widget(self.user_age)
        #country label widget
        self.ask_location = Label(text="\n Where are you from?")
        self.window.add_widget(self.ask_location)
        #country text input widget
        self.user_location = TextInput(multiline=False)
        self.window.add_widget(self.user_location)

        #BUTTON WIDGET
        self.button = Button(text="Start your mindfulness journey!",
                             bold = True,
                             background_color = "#99AFD7",
                             background_normal = "")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        """
        Changes text in greeting to match user's name input
        """
        self.greeting.text = "Hello " + self.user.text + "!"

    
if __name__ == "__main__":
    app = FERApp()
    app.run()