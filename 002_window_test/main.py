from kivy.clock import Clock
from kivy.app import App
from kivy.config import Config
from kivy.uix.textinput import TextInput

Config.set('graphics', 'window_state', 'hidden')

class MyDebugApp(App):
    visible = False
    def build(self):
        return TextInput()

    def on_start(self):
        Clock.schedule_interval(self.alternate, 5)
        self.root.focus = True

    def alternate(self, dt):
        if self.visible:
            self.root.get_root_window().hide()
        else:
            self.root.get_root_window().show()

        self.visible = not self.visible


if __name__ == "__main__":
    ma = MyDebugApp().run()