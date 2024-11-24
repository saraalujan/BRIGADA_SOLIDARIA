from kivy_garden.mapview import MapView, MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
import geocoder

class Root(BoxLayout):
    map = ObjectProperty()
    def point(self, x, y):
        marker = MapMarker(lon=y, lat=x)
        self.map.add_marker(marker)
    pass
class MapViewApp(App):
    pass
MapViewApp().run()