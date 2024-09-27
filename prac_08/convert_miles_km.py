"""
CP1404 - Covnert Mile to KM using GUI and python

Estimate time: 1hour
Actual time: 2hours
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KILOMETER_TO_MILES = 1.609344


class ConvertMilesKmApp(App):
    """Main program - Kivy app to convert miles to km."""
    result = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_miles_to_km(self):
        """Convert miles to km and return in str as result."""
        km = self.validate_miles() * KILOMETER_TO_MILES
        self.result = str(km)

    def validate_miles(self):
        """Validate miles and return it"""
        try:
            miles = float(self.root.ids.input_number.text)
        except ValueError:
            miles = 0.0
        return miles

    def handle_increment(self, change):
        """Change miles using up or down button by 1 and convert it to km."""
        miles = int(self.validate_miles() + change)
        self.root.ids.input_number.text = str(miles)
        self.handle_miles_to_km()


ConvertMilesKmApp().run()

