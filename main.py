from kivy.app import App

class HelloKivy(App):
    def build(self):
        # No need to return Label here, since the .kv file will handle it
        return None

KivyApp = HelloKivy()
KivyApp.run()
