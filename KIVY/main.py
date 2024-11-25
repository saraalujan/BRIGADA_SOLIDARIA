from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from sqlalchemy import create_engine, text

# Configurar tamaño y color de fondo de la ventana
Window.size = (400, 600)
Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Fondo claro

class FormularioScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=20, padding=30, **kwargs)

        # Inicializar el diccionario 'inputs' para almacenar los campos de texto
        self.inputs = {}

        # Título del formulario
        self.add_widget(Label(
            text="Registro de Casos",
            font_size=24,
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            size_hint=(1, 0.2),
            halign="center"
        ))

        # Campo para Dirección
        self.add_widget(self.crear_campo("Dirección:", "Ingrese la dirección"))

        # Campo para Adultos
        self.add_widget(self.crear_campo("Cantidad de Adultos:", "Ingrese la cantidad de adultos", input_filter="int"))

        # Campo para Menores
        self.add_widget(self.crear_campo("Cantidad de Menores:", "Ingrese la cantidad de menores", input_filter="int"))

        # Botón para Enviar
        self.boton_enviar = Button(
            text="Enviar Datos",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1),
            font_size=18
        )
        self.boton_enviar.bind(on_press=self.enviar_datos)
        self.add_widget(self.boton_enviar)

    def crear_campo(self, etiqueta, placeholder, input_filter=None):
        """Crea un campo de entrada con etiqueta y campo de texto."""
        layout = BoxLayout(orientation='vertical', spacing=5, size_hint=(1, 0.3))

        label = Label(
            text=etiqueta,
            font_size=16,
            size_hint=(1, 0.4),
            color=(0.2, 0.2, 0.2, 1),
            halign="left",
            valign="middle"
        )
        label.bind(size=label.setter('text_size'))  # Alineación vertical
        layout.add_widget(label)

        input_text = TextInput(
            hint_text=placeholder,
            multiline=False,
            padding=(10, 10),
            size_hint=(1, 0.6),
            background_color=(0.9, 0.9, 0.9, 1),
            foreground_color=(0, 0, 0, 1),
            cursor_color=(0.2, 0.6, 0.8, 1),
            font_size=14,
            input_filter=input_filter
        )
        layout.add_widget(input_text)

        # Guardar la referencia al campo de texto
        self.inputs[etiqueta] = input_text
        return layout

    def enviar_datos(self, instance):
        # Obtener datos del formulario
        direccion = self.inputs["Dirección:"].text
        adultos = self.inputs["Cantidad de Adultos:"].text
        menores = self.inputs["Cantidad de Menores:"].text

        # Validación
        if not direccion:
            self.mostrar_popup("Error", "Por favor, complete todos los campos correctamente.")
        else:
            try:
                adultos = int(adultos)
            except ValueError:
                self.mostrar_popup("Error", "La cantidad de adultos debe ser un número válido.")
                return
            
            try:
                menores = int(menores)
            except ValueError:
                self.mostrar_popup("Error", "La cantidad de menores debe ser un número válido.")
                return
            
            # Aquí procesarías los datos y los insertas en la base de datos
            try:
                self.insertar_datos_en_bd(direccion, adultos, menores)
                self.mostrar_popup("Éxito", "Datos enviados y guardados correctamente.")
            except Exception as e:
                self.mostrar_popup("Error", f"Ocurrió un error al guardar los datos: {str(e)}")

    def mostrar_popup(self, titulo, mensaje):
        """Muestra un popup con un mensaje dado."""
        popup = Popup(
            title=titulo,
            content=Label(
                text=mensaje,
                halign="center",
                valign="middle",
                color=(0.2, 0.2, 0.2, 1),
                font_size=16
            ),
            size_hint=(0.8, 0.4)
        )
        popup.open()


class FormularioApp(App):
    def build(self):
        return FormularioScreen()


if __name__ == "__main__":
    FormularioApp().run()
