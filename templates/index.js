$(document).ready(function () {
    console.log('index.js')

    var map = clear_map() //инициируем карту

    function clear_map() { //тут началo
        console.log('clear_map')
        let layerSelect = new ol.layer.Tile({ source: new ol.source.OSM() })
        return new ol.Map({
            target: 'map_area',
            layers: [layerSelect],
            view: new ol.View({ center: ol.proj.fromLonLat([58.0, 60.0]), zoom: 2 }),
            //controls: [], // отключает подпись к карте
        });
    }


    function point(X, Y, device_id, name) { // создание Устройства или сигналы на карте
        let iconFeature = new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.transform([X, Y], 'EPSG:4326', 'EPSG:3857')),
            device_id: device_id,
            name: name,
            X: X, //layerInfo.get('X'),
            Y: Y, // layerInfo.get('Y'),
        });
        let pic = 'templates/img/ico.png';
        let iconStyle = new ol.style.Style({
            // anchor - якорь, точка в которой создается картинка [0.5, 1] - отступы по X, Y
            // 0.5 при anchorXUnits: 'fraction' - отступ на 50% от размера картинки
            image: new ol.style.Icon({ anchor: [0.5, 1], anchorXUnits: 'fraction', anchorYUnits: 'fraction', src: pic, scale: 1 })
        });
        iconFeature.setStyle(iconStyle);
        let vectorSource = new ol.source.Vector({
            features: [iconFeature],
        });
        let vectorLayer = new ol.layer.Vector({ //OpenLayers.Layer.OSM
            source: vectorSource,
            name: 'selectable', //
            title: device_id, // добавить в описание device_id для удаления ($('.delete_object'))
        });
        return vectorLayer;
    }



    $(document).on('click', '#import_kml', function () {
        let file = document.getElementById('file').files[0]
        let formData = new FormData();
        formData.append("file", file);
        $.ajax({
            headers: {
                Accept: "application/json"
            },
            type: "POST",
            enctype: "multipart/form-data",
            cache: false,
			contentType: false,
			processData: false,
			data: formData,
			dataType : 'json',
            url: '/uploadfile',
            data: formData,
            success: function(data){
                $("#table_points .body_row").remove();
                let wells = data['wells']
                let tbodyRef = document.getElementById('table_points').getElementsByTagName('tbody')[0];
                for (let i = 0; i < wells.length; i++) {
                    let well = wells[i]
                    let coord_x = well['coordinates'][0]['x']
                    let coord_y = well['coordinates'][0]['y']
                    let name = well['name']
                    let id = well['id']
                    //  Отрисовка точек на карте
                    console.log(coord_x, coord_y)
                    map.addLayer(point(coord_x, coord_y, id, name));
                    //  Заполнение таблицы
                    let newRow = tbodyRef.insertRow();
                    newRow.setAttribute('class', 'body_row')
                    let newCell1 = newRow.insertCell();
                    let newText1 = document.createTextNode(name);
                    newCell1.appendChild(newText1);
                    let newCell2 = newRow.insertCell();
                    let newText2 = document.createTextNode(coord_x);
                    newCell2.appendChild(newText2);
                    let newCell3 = newRow.insertCell();
                    let newText3 = document.createTextNode(coord_y);
                    newCell3.appendChild(newText3);
                    let newCell4 = newRow.insertCell();
                    let newText4 = document.createTextNode(0);
                    newCell4.appendChild(newText4);
                    let newCell5 = newRow.insertCell();
                    let newText5 = document.createTextNode('');
                    newCell5.appendChild(newText5);
                }
                console.log(wells)
            }
        });

    })

    $(document).on('click', '#clear_points', function () {
        //  Очистка таблицы
        $("#table_points .body_row").remove();
        // Очистка точек на карте
        let layerArray, len, layer;
        layerArray = map.getLayers().getArray(),
            len = layerArray.length;
        while (len > 1) { // Удаляем все сигналы с карты для перерисовки
            layer = layerArray[len - 1];
            map.removeLayer(layer);
            len = layerArray.length; // каждую итерацию уменьшается на 1
        }
    })
})
