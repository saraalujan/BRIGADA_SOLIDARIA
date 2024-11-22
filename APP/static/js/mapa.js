$(document). ready(function(){
    const mapa = document.getElementById('mapacentros');
    const map = L.map(mapa).setView([-34.60473, -58.38664], 14);



    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var url = 'http://root:1234@localhost:5001/api/v1/centros/direcciones';

    function obtenerCoordenadas(direccion, callback){
        var apiUrl = 'https://nominatim.openstreetmap.org/search?q=' + encodeURIComponent(direccion) + '&format=json';

        $.get(apiUrl, function(dqata) {
            if (data && data.length > 0) {
                var lat = data[0].lat;
                var lon = data[0].lon;
                callback(lat, lon);
            }
        });
    }

    $.getJSON(url, function(direcciones){
        direcciones.forEach(function(item){
            obtenerCoordenadas(item.direccion, function(lat, lon){
                L.marker([lat, lon])
                    .addTo(map)
                    .bindPopup('<b>' + item.nombre + '</b><b>' + item.direccion);
            });
        });
    }).fail(function(){
        alert('No se pudo cargar el archivo JSON')
    });
});
