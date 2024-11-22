const mapa = document.getElementById('mapacentros');
const map = L.map(mapa).setView([19.04, -98.187], 14);



L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


const getData = async () => {
    const responseCentros = await fetch('http://root:1234@localhost:5001/api/v1/centros/direcciones');
    const dataCentros = await responseCentros.json();
}

getData();