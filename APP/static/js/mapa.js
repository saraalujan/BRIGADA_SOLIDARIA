document.addEventListener("DOMContentLoaded", function () {
    // Inicializar el mapa centrado en una ubicación predeterminada
    const map = L.map("map").setView([-34.6083, -58.3712], 13); // Centro en Buenos Aires

    // Cargar la capa base de OpenStreetMap
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Obtener direcciones desde el endpoint
    async function obtenerDirecciones() {
        try {
            const respuesta = await fetch('http://127.0.0.1:5001/api/v1/centros/direcciones');
            const datos = await respuesta.json();
            return datos; // Se espera un array de direcciones
        } catch (error) {
            console.error("Error al obtener las direcciones:", error);
            return [];
        }
    }

    // Geocodificar una dirección usando Nominatim
    async function geocodificarDireccion(direccion) {
        const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(direccion + ", Ciudad Autónoma de Buenos Aires, Argentina")}&accept-language=es`;
        try {
            console.log(`Solicitando coordenadas para: ${direccion}`);
            const respuesta = await fetch(url);
            const datos = await respuesta.json();
            console.log("Datos recibidos de Nominatim:", datos);

            // Si hay al menos tres resultados, intentamos encontrar el adecuado
            if (datos.length >= 3) {
                // Intentamos seleccionar la opción que contenga "Ciudad Autónoma de Buenos Aires"
                for (let i = 0; i < datos.length; i++) {
                    if (datos[i].display_name.includes("Ciudad Autónoma de Buenos Aires")) {
                        return {
                            lat: parseFloat(datos[i].lat),
                            lon: parseFloat(datos[i].lon),
                            nombre: direccion
                        };
                    }
                }
                // Si no encontramos una opción con "Ciudad Autónoma de Buenos Aires", seleccionamos la tercera opción
                return {
                    lat: parseFloat(datos[2].lat),
                    lon: parseFloat(datos[2].lon),
                    nombre: direccion
                };
            } else if (datos.length > 0) {
                // Si no hay tres resultados, pero al menos uno, seleccionamos el primero
                return {
                    lat: parseFloat(datos[0].lat),
                    lon: parseFloat(datos[0].lon),
                    nombre: direccion
                };
            } else {
                console.warn(`No se encontraron coordenadas para: ${direccion}`);
                return null;
            }
        } catch (error) {
            console.error("Error al geocodificar la dirección:", error);
            return null;
        }
    }

    // Función principal: Obtener direcciones y mostrarlas en el mapa
    async function mostrarDireccionesEnMapa() {
        const direcciones = await obtenerDirecciones();
        console.log("Direcciones obtenidas:", direcciones);

        for (const direccion of direcciones) {
            const coordenadas = await geocodificarDireccion(direccion.direccion);
            if (coordenadas) {
                const marker = L.marker([coordenadas.lat, coordenadas.lon]).addTo(map);
                marker.bindPopup(`<b>${coordenadas.nombre}</b><br>Lat: ${coordenadas.lat}, Lon: ${coordenadas.lon}`);
            }
        }
    }

    // Llamar a la función para mostrar las direcciones en el mapa
    mostrarDireccionesEnMapa();
});