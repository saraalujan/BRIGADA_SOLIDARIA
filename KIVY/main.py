import json
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy_garden.mapview import MapView, MapMarker
from kivy.network.urlrequest import UrlRequest
import requests
from kivy.lang import Builder  # Para cargar el archivo .kv

# Pantalla Principal
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def go_to_map(self):
        self.manager.current = "map_screen"

    def go_to_form(self):
        self.manager.current = "form_screen"


class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # La inicialización de `map_view` ahora se hará desde el archivo .kv usando el id
        self.map_view = None

    def on_enter(self):
        # Este método se llama cuando la pantalla se activa
        self.map_view = self.ids.mapview  # Asignar el MapView usando el id del archivo .kv

    def mostrar_casos(self, instance):
        print("Solicitando datos...")
        # Realizar la solicitud a la API usando UrlRequest
        url = "http://127.0.0.1:5001/api/v1/casos"  # Cambia esta URL por la de tu API
        UrlRequest(url, on_success=self.on_success, on_failure=self.on_failure)

    def obtener_coordenadas(self, direccion):
        # Definir los límites geográficos de la Ciudad Autónoma de Buenos Aires (CABA)
        lat_min = -34.8
        lat_max = -34.5
        lon_min = -58.5
        lon_max = -58.3

        # Usar Nominatim para obtener las coordenadas (lat y lon) de una dirección dentro de CABA
        geocode_url = f"https://nominatim.openstreetmap.org/search?q={direccion}&format=json&addressdetails=1&bounded=1&viewbox={lon_min},{lat_max},{lon_max},{lat_min}&extratags=1"

        # Definir el encabezado User-Agent requerido por Nominatim
        headers = {
            'User-Agent': 'MapApp/1.0'  # Cambia esto por tu email o un identificador apropiado
        }

        # Hacer la solicitud con el encabezado User-Agent
        response = requests.get(geocode_url, headers=headers)
        
        # Verificar si se encontró una respuesta válida
        data = response.json()
        if data:
            # Extraer las coordenadas
            latitud = float(data[0]['lat'])
            longitud = float(data[0]['lon'])
            return latitud, longitud
        else:
            return None, None  # No se encontraron coordenadas

    def on_success(self, request, result):
        # Imprimir la respuesta completa para verificar su formato
        print(f"Respuesta completa recibida: {result}")

        try:
            # Asegurarnos de que la respuesta es una lista
            if isinstance(result, list):
                print("Procesando los casos...")

                # Evitar limpiar los widgets del mapa, solo agregamos los nuevos marcadores
                for caso in result:
                    direccion = caso.get('direccion')

                    # Usar Nominatim para obtener las coordenadas de la dirección dentro de CABA
                    latitud, longitud = self.obtener_coordenadas(direccion)

                    if latitud and longitud:
                        print(f"Marcador: lat={latitud}, lon={longitud}")
                        # Agregar marcador al mapa
                        marker = MapMarker(lat=latitud, lon=longitud)
                        self.map_view.add_widget(marker)
                    else:
                        print(f"No se encontraron coordenadas para la dirección: {direccion}")
            else:
                print("La respuesta no es una lista como se esperaba.")
        except Exception as e:
            print(f"Error al procesar la respuesta: {e}")

    def on_failure(self, request, error):
        print(f"Error al cargar los casos: {error}")

    def go_to_main(self):
        self.manager.current = "main_screen"


# Pantalla del Formulario
class FormScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def submit_form(self, direccion, adultos, menores):
        data = {
            "direccion": direccion,
            "adultos": int(adultos),
            "menores": int(menores)
        }

        json_data = json.dumps(data)
        url = "http://127.0.0.1:5001/api/v1/anadircaso"
        headers = {'Content-Type': 'application/json'}

        UrlRequest(url, req_body=json_data, method='POST', on_success=self.on_success, on_failure=self.on_failure, req_headers=headers)

    def on_success(self, request, result):
        print("Datos enviados exitosamente", result)
        # Mostrar mensaje de éxito en la pantalla del formulario
        self.ids.message_label.text = "¡Caso añadido con éxito!"

    def on_failure(self, request, error):
        print(f"Error al enviar los datos: {error}")
        # Mostrar mensaje de error en la pantalla del formulario
        self.ids.message_label.text = "Error al añadir el caso."

    def go_to_main(self):
        self.manager.current = "main_screen"


# Aplicación principal
class MyApp(MDApp):
    def build(self):
        Builder.load_file("main.kv")  # Asegúrate de cargar el archivo .kv aquí
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="main_screen"))
        screen_manager.add_widget(MapScreen(name="map_screen"))
        screen_manager.add_widget(FormScreen(name="form_screen"))
        return screen_manager

# Ejecutar la aplicación
if __name__ == "__main__":
    MyApp().run()
