from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properies import BooleanProperty

class ObjectDetectionView(Widget):   
    editable = BooleanProperty(True)
    def __init__(self, **kwargs):
        super(ObjectDetectionView, self).__init__(**kwargs)
