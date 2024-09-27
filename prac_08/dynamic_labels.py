"""
CP1404 - Dynamically create labels based on content of list
Estimate time: 2hours
Actual time: 1hour
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to dynamic labels creation."""
    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Olivia", "John", "Mandy", "David", "Jennie"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.names:
            label = Label(text = name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()

