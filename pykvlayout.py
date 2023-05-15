
# Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns --- logo and welcome message
        self.cols = 1
        self.size_hint = (0.6, 0.7)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}  
        self.row_force_default = True
        self.row_default_height = 70
        self.col_force_default = True
        self.col_default_width = 420

        # Create second grid layout --- user input boxes
        self.form_grid = GridLayout(row_force_default=True,
                                    row_default_height = 50,
                                    col_force_default = True,
                                    col_default_width = 200)
        self.form_grid.cols = 2
        self.form_grid.size_hint = (0.6, 0.7)
        self.form_grid.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Third grid layout --- button
        self.button_grid = GridLayout(col_force_default = True,
                                      col_default_width = 420,
                                      row_force_default = True,
                                      row_default_height = 100)
        
        self.button_grid.cols = 1
        self.button_grid.size_hint = (0.6, 0.7)
        self.button_grid.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # ADD WIDGETS
        # Welcome msg and logo
        self.add_widget(Image(source="fruit_img.png"))
        self.greeting = Label(text="Hello from Kivy",
                              font_size = 22)
        self.add_widget(self.greeting)
        self.welcome_msg = Label(text="Welcome to your daily journal!",
                                 font_size=20,
                                 line_height = .1)
        self.add_widget(self.welcome_msg)

        # add input box grid widget
        self.add_widget(self.form_grid)
        # Username input box
        self.form_grid.add_widget(Label(text="Username:",
                                        font_size=16))
        self.username = TextInput(multiline=False)
        self.form_grid.add_widget(self.username)
        # Password input box
        self.form_grid.add_widget(Label(text="Password:",
                                        font_size=16))
        self.password = TextInput(multiline=False)
        self.form_grid.add_widget(self.password)

        # add button grid
        self.add_widget(self.button_grid)
        # Login button
        self.login_button = Button(text="Login",
                                   font_size=30,
                                   bold = True,
                                   background_color = "#99AFD7",
                                   background_normal = "",
                                   size_hint_y = None,
                                   height = 45,
                                   width = 190)
        # Bind button
        self.login_button.bind(on_press=self.press)
        self.button_grid.add_widget(self.login_button)