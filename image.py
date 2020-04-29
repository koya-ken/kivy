from kivy.config import Config
Config.set('modules', 'inspector', '')
# 右クリックで赤丸がでるのを抑止する
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
import numpy as np
from kivy.graphics.texture import Texture
from event import ClickEvent
from event import ImageClickEvent
from event import ClickEventCode
from data import CollisionManager

def create_texture():
    width = 800
    height = 400
    color = (255,0,0)
    img = np.full((height,width,3),color,dtype=np.uint8)
    img[:,int(width/2):] = (0,255,0)
    texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい
    texture.blit_buffer(img.tostring(),colorfmt='bgr', bufferfmt='ubyte')  # ★ここもここもBGRで指定しないとRGBになって色の表示がおかしくなる
    texture.flip_vertical()    # 画像を上下反転する
    return texture


class ImageWidget(Widget):
    image = ObjectProperty(None)
    image_texture = ObjectProperty(None)
    clickevent = None
    collisionmanager = None

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        self.image_texture = create_texture()
        self.clickevent = ImageClickEvent(widget_size=self.size,image_size=[0,0])
        self.collisionmanager = CollisionManager()
        pass
    def on_touch_down(self, touch):
        self.clickevent.update(ClickEventCode.DOWN,self.image,touch)
        print("aaaaaaaaaaaaaaa",self.to_local(*touch.pos))
    def on_touch_move(self, touch):
        self.clickevent.update(ClickEventCode.MOVE,self.image,touch)
    def on_touch_up(self, touch):
        self.clickevent.update(ClickEventCode.UP,self.image,touch)
    def on_size(self,target_view,size):
        self.clickevent.update_widget_size(self.image,size)

class TestApp(App):
    def on_start(self):
        print('on_start',self.root.image)
        pass

if __name__ == '__main__':
    TestApp().run()
