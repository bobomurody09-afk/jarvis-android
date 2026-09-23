from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class JarvisApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.scroll = ScrollView()
        self.chat_label = Label(
            size_hint_y=None,
            text="JARVIS: Salom! Sizga qanday yordam bera olaman?\n",
            halign='left',
            valign='top'
        )
        self.chat_label.bind(texture_size=self._update_label_height)
        self.scroll.add_widget(self.chat_label)
        self.layout.add_widget(self.scroll)

        self.input_box = TextInput(size_hint_y=None, height=50, multiline=False)
        self.input_box.bind(on_text_validate=self.send_message)
        self.layout.add_widget(self.input_box)

        send_btn = Button(text="Yuborish", size_hint_y=None, height=50)
        send_btn.bind(on_press=self.send_message)
        self.layout.add_widget(send_btn)

        return self.layout

    def _update_label_height(self, instance, size):
        instance.height = size[1]
        instance.width = self.scroll.width
        instance.text_size = (self.scroll.width, None)

    def send_message(self, *args):
        user_text = self.input_box.text.strip()
        if not user_text:
            return
        self.chat_label.text += f"\nSiz: {user_text}\n"
        self.input_box.text = ""
        response = self.get_response(user_text)
        self.chat_label.text += f"JARVIS: {response}\n"

    def get_response(self, text):
        return "Hozircha men oddiy javob beryapman. API keyin ulanadi."


if __name__ == '__main__':
    JarvisApp().run()
