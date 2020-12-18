

# App Title: Words of Light
# Description:
# Key Features:
#     - light and dark mode
#     - share any devotional with your friends and family (messenger, fb, copy to clipboard, etc.)
#     - get notified when the devotionals are available (notification)
#     - save your favorite devotionals to read lateror to reference (save to file)
#     - New Bible trivia each day to test your Bible knowledge (import from file)
#     - Connect to other people with our growing community (join to a group)
#     - Make your own group chats and discuss your devotionals (add friend to form group)
#
# Profile:
#     - Name
#     - Faith Motto
#     - Email
#     - BDate
#     - Account Pic
#     - Change Password
#
# Community:
#     - Share Devotions
#     - FAQs
#     - Q&A
#
# Settings:
#     - Notification
#     - About
#     - Version


# KIVY Libraries
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty, ListProperty

# KIVYMD Libraries
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker

# Themes, Components, Behaviors
from kivymd.uix.list import MDList
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem, ThreeLineAvatarListItem
from kivymd.theming import ThemeManager, ThemableBehavior
from kivymd.uix.list import MDList, OneLineListItem, ThreeLineIconListItem
from kivymd.uix.list import ImageLeftWidget, ImageRightWidget
from kivymd.uix.dialog import MDDialog


# PRE-EMPTIVE CLASSES
class WindowManager(ScreenManager):
    pass

class LoadWindow(Screen):
    pass

class IntroWindow1(Screen):
    pass

class IntroWindow2(Screen):
    pass

class IntroWindow3(Screen):
    pass

class IntroWindow4(Screen):
    pass

class RegisterWindow(Screen):
    pass

class LoginWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class Profile(Screen):
    pass

class Devotions(Screen):
    pass

class Community(Screen):
    pass

class Bookmark(Screen):
    pass

class Settings(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoadWindow(name='load'))
sm.add_widget(IntroWindow1(name='intro'))
sm.add_widget(IntroWindow2(name='intro2'))
sm.add_widget(IntroWindow3(name='intro3'))
sm.add_widget(IntroWindow4(name='intro4'))
sm.add_widget(RegisterWindow(name='register'))
sm.add_widget(LoginWindow(name='login'))
sm.add_widget(MainWindow(name='main'))
sm.add_widget(Profile(name='profile'))
sm.add_widget(Devotions(name='devotions'))
sm.add_widget(Community(name='community'))
sm.add_widget(Bookmark(name='bookmarks'))
sm.add_widget(Settings(name='settings'))
sm.current = "load"

Window.size = (350, 600)

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.title = "Words of Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        # self.root = Builder.load_file("ux_main.kv")
        return Builder.load_file("ux_main.kv")

    def on_start(self):
        pass


if __name__ == "__main__":
    MainApp().run()
