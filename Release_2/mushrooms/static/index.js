(function (window) {
    'use strict';

    function initMap() {
        var control;
        var L = window.L;
        var basic = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; 2013 OpenStreetMap contributors'
        }),
            streets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}', {
            minZoom: 2,
            maxZoom: 18,
            subdomains:['mt0','mt1','mt2','mt3'],
            attribution: 'Map data &copy; 2018 Google'
        }),
            altstreets = L.tileLayer('http://{s}.google.com/vt/lyrs=r&hl=en&x={x}&y={y}&z={z}', {
            minZoom: 2,
            maxZoom: 18,
            subdomains:['mt0','mt1','mt2','mt3'],
            attribution: 'Map data &copy; 2018 Google'
        }),
            hybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}', {
            minZoom: 2,
            maxZoom: 18,
            subdomains:['mt0','mt1','mt2','mt3'],
            attribution: 'Map data &copy; 2018 Google'
        }),
            satellite = L.tileLayer('http://{s}.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}', {
            minZoom: 2,
            maxZoom: 18,
            subdomains:['mt0','mt1','mt2','mt3'],
            attribution: 'Map data &copy; 2018 Google'
        }),
            terrain = L.tileLayer('http://{s}.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}', {
            minZoom: 2,
            maxZoom: 18,
            subdomains:['mt0','mt1','mt2','mt3'],
            attribution: 'Map data &copy; 2018 Google'
        });
        var map = L.map('map', {
            center: [0, 0],
            zoom: 2
        }).addLayer(hybrid);
        var baseMaps = {
            "Basic": basic,
            "Streets": streets,
            "Alt Streets": altstreets,
            "Hybrid": hybrid,
            "Satellite": satellite,
            "Terrain": terrain
        }

        L.control.layers(baseMaps).addTo(map);

        L.Control.FileLayerLoad.LABEL = '<img class="icon" src="/static/folder.svg" alt="file icon"/>';
        control = L.Control.fileLayerLoad({
            fitBounds: true,
            layerOptions: {
                pointToLayer: function (data, latlng) {
                    var path = data.properties.description.split('"')[3]
                    var href = '<button class="btn btn-warning" style="width:10rem;"><a class="text-dark" style="text-decoration:none;" href="/email/' + path + '">Send Image</a></button>'
                    return L.marker(latlng).bindPopup(data.properties.description + href, {minWidth:300, maxWidth:1000});
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
