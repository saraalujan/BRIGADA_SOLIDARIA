from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarker
from plyer import gps
from kivy.clock import Clock

class MyApp(App):
    def build(self):
        # Crear el layout
        layout = BoxLayout(orientation='vertical')
        
        # Crear el widget MapView
        self.map_view = MapView(zoom=15, lat=0, lon=0)  # Inicializar con coordenadas arbitrarias
        layout.add_widget(self.map_view)

        # Iniciar el GPS
        gps.configure(on_location=self.on_location)  # Establece la función de callback
        gps.start()

        return layout

    def on_location(self, **kwargs):
        # Obtener la ubicación del usuario
        lat = kwargs.get('lat', 0)
        lon = kwargs.get('lon', 0)
        
        # Actualizar el mapa con la nueva ubicación
        self.map_view.center_on(lat, lon)
        
        # Crear un marcador en la ubicación
        marker = MapMarker(lat=lat, lon=lon)
        self.map_view.add_widget(marker)

    def on_stop(self):
        # Detener el GPS al cerrar la app
        gps.stop()

if __name__ == "__main__":
    MyApp().run()