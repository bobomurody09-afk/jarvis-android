from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class JarvisApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.label = Label(
            text="J.A.R.V.I.S\n\nTayyor",
            font_size=28
        )

        button = Button(
            text="🎙 GAPIRISH",
            font_size=24,
            size_hint_y=None,
            height=80
        )

        button.bind(on_press=self.test)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def test(self, instance):
        self.label.text = "J.A.R.V.I.S\n\nMikrofon tayyorlanmoqda..."


JarvisApp().run()
