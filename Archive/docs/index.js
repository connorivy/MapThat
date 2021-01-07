(function (window) {
    'use strict';

    function initMap() {
        var control;
        var L = window.L;
        var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; 2013 OpenStreetMap contributors'
        });
        var map = L.map('map', {
            center: [0, 0],
            zoom: 2
        }).addLayer(osm);

        L.Control.FileLayerLoad.LABEL = '<img class="icon" src="folder.svg" alt="file icon"/>';
        control = L.Control.fileLayerLoad({
            fitBounds: true,
            layerOptions: {
                pointToLayer: function (data, latlng) {
                    return L.marker(latlng).bindPopup('A pretty CSS3 popup.<br> Easily customizable.');
                }
            }
        });

        control.addTo(map);

        control.loader.on('data:loaded', function (e) {
            var layer = e.layer;
            console.log(layer);
        });
    }

    window.addEventListener('load', function () {
        initMap();
    });
}(window));
