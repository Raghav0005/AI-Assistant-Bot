#Elaborated using kivymd

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window

Window.size = (300,500)

screen_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Voice Assistant App'
                        left_action_items:[['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    MDLabel:
                        text: 'Welcome!'
                        halign: 'center'
                    MDBottomAppBar:
                        MDToolbar:
                            type: 'bottom'
                            icon: 'microphone'
                            
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                MDLabel:
                    text: 'Voice Assistant Prototype App'
                    font_style: 'Subtitle1'
                    size_hint_y:None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'Hackathon: Hack the North'
                    font_style: 'Caption'
                    size_hint_y:None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Settings'
                            IconLeftWidget:
                                icon: 'nut'
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face'

"""


class VAApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

        
VAApp().run()
