from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(
            text="HELLO FROM PYTHON",
            font_size="24sp"
        )


TestApp().run()