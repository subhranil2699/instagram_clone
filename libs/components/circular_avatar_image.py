from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class CircularAvatarImage(MDCard):
    avatar = StringProperty()
    name = StringProperty()