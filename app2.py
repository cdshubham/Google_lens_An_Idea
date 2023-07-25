from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from plyer import filechooser
# from kivy.core.window import Window

# My Modules
import QrCdOn
import TextAudio
import Text_detection
import ImageClassification
import lang_translate


selected_file = ""

# Main layout for Screen(Custom Widget) inherites from BoxLayout


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        # Set orientation
        self.orientation = 'vertical'

        # Set background image
        background = Image(source="glens1.png")
        self.add_widget(background)

        # Create button container
        button_container = BoxLayout(
            orientation='horizontal', size_hint=(1, 0.1))

        # Create buttons
        button1 = Button(text='QR Detect', size_hint=(0.20, 1))
        button2 = Button(text='Image to Text', size_hint=(0.20, 1))
        button3 = Button(text='Image to Audio', size_hint=(0.20, 1))
        button4 = Button(text='Object Detection', size_hint=(0.20, 1))
        button5 = Button(text='Translate', size_hint=(0.20, 1))
        # Add buttons to the container
        button_container.add_widget(button1)
        button_container.add_widget(button2)
        button_container.add_widget(button3)
        button_container.add_widget(button4)
        button_container.add_widget(button5)

        button1.bind(on_press=self.on_button1_click)
        button2.bind(on_press=self.on_button2_click)
        button3.bind(on_press=self.on_button3_click)
        button4.bind(on_press=self.on_button4_click)
        button5.bind(on_press=self.on_button5_click)
        # Add the button container to the root widget
        self.add_widget(button_container)

    def on_button1_click(self, instance):
        QrCdOn.hell()

    def on_button2_click(self, instance):
        Text_detection.textDetect()

    def on_button3_click(self, instance):
        TextAudio.textToAudio()

    def on_button4_click(self, instance):
        ImageClassification.ImageClassify()

    def on_button5_click(self, instance):
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        if len(selection) > 0:
            selected_file = selection[0]
            lang_translate.translation(selected_file)


class MyApp(App):
    def build(self):
        return RootWidget()


MyApp().run()
