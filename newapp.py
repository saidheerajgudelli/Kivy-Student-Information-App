import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Set the background color of the window (optional)
Window.clearcolor = (0.2, 0.2, 0.2, 1)  # Dark grey background

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__(**kwargs)
        self.cols = 2
        self.padding = 10  # Add padding around the layout
        self.spacing = 10  # Add spacing between widgets

        # Label and TextInput for Student Name
        self.add_widget(Label(text='Student Name', color=(0, 1, 0, 1), font_size=20))  # Green label
        self.s_name = TextInput(foreground_color=(1, 1, 1, 1), background_color='white')  # Blue input box with white text
        self.add_widget(self.s_name)

        # Label and TextInput for Student Marks
        self.add_widget(Label(text='Student Marks', color=(1, 1, 0, 1), font_size=20))  # Yellow label
        self.s_marks = TextInput(foreground_color=(1, 1, 1, 1), background_color='white')  # Green input box with white text
        self.add_widget(self.s_marks)

        # Label and TextInput for Student Gender
        self.add_widget(Label(text='Student Gender', color=(1, 0, 1, 1), font_size=20))  # Purple label
        self.s_gender = TextInput(foreground_color=(1, 1, 1, 1), background_color='white')  # Red input box with white text
        self.add_widget(self.s_gender)

        # Button with a different color and style
        self.press = Button(text='Submit', font_size=24, background_color=(0, 0.5, 0.8, 1), color=(1, 1, 1, 1))  # Cyan button with white text
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print('Name of the student is: ' + self.s_name.text)
        print('Marks of the student is: ' + self.s_marks.text)
        print('Gender of the student is: ' + self.s_gender.text)
        print(' ')

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()
