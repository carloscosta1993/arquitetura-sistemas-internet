/**
 * Created by carloscosta on 21-12-2016.
 */

$(document).ready(function () {

        var campus_id = "campusList";
        var new_campus_id;

        document.getElementById("campus").onclick = function () {
            if (document.getElementById("selection").style.display == "block")
            {
                document.getElementById("selection").style.display = "none";
                document.getElementById("selection").innerHTML = "";
            }else{
                document.getElementById("selection").style.display = "block";
                get_all_spaces(campus_id);
            }
        };

        $('#selection').on('change', function() {
            new_campus_id = $(this).children('select').last('select').find(':selected').attr('value');
            var room = $(this).children('select').last('select').find(':selected').text();
            get_all_spaces(new_campus_id, room);
        });

        document.getElementById("roomsButton").onclick = function () {
            if (document.getElementById("rooms").style.display == "block")
            {
                document.getElementById("rooms").style.display = "none";
            }else{
                document.getElementById("rooms").style.display = "block";
            }
        };

        $('#roomsTable').on('click', 'input[type="button"]', function(e){
            $(this).closest('tr').remove();
            deleteRow($(this).closest('tr')[0].cells[0].innerHTML, $(this).closest('tr')[0].cells[1].innerHTML)
        });

    function findValue(room){
            var table = document.getElementById('roomsTable');
            for(var i=1;i<table.rows.length;i++) {
                var trs = table.getElementsByTagName("tr")[i];
                var cellVal = trs.cells[0].innerHTML;
                if(cellVal == room ){
                    return true
                }
            }

        }

    function deleteRow(room) {
                    $.ajax({
                        type: "DELETE",
                        async: false,
                        url: "/delete_room/" + room
                 });
                }


    function getCampus() {
            var data;
                    $.ajax({
                        type: "GET",
                        async: false,
                        url: "/get_campus",
                        success: function(response){
                                data = JSON.parse(response);
                        }
                 });
             return data;
                }

    function getData(id) {
            var data;
                    $.ajax({
                        type: "POST",
                        async: false,
                        url: "/get_data/" + id,
                        success: function(response){
                                data = JSON.parse(response);
                        }
                 });
            return data;
                }

    function storeRoom(room, capacity) {
                    $.ajax({
                        type: "POST",
                        async: false,
                        url: "/store_data/" + room + "/" + capacity
                 });
                }

    function get_all_spaces(campus_id, room)
        {
            var data;
            var roomData;
            var capacity;
            var myDiv = document.getElementById("selection");
            if(campus_id == "campusList"){
                data = getCampus();
                var selectList = document.createElement("select");
                selectList.id = campus_id;
                selectList.classList = "form-control";
                myDiv.appendChild(selectList);
                var option1 = document.createElement("option");
                option1.text = "CAMPUS";
                selectList.appendChild(option1);
                 $.each(data, function(idx, item){
                    var option = document.createElement("option");
                    option.value = item.id;
                    option.text = item.name;
                    selectList.appendChild(option);
                });
            }else{
                data = getData(campus_id);
                if(data['containedSpaces'].length == 0){
                    var equal_room = findValue(data['name']);
                    if (equal_room == true)
                    {
                        alert("ROOM ALREADY ADDED!");
                    }else {
                        storeRoom(data['name'], data['capacity']['normal']);
                        var button = document.createElement('input');
                        button.setAttribute('class', 'btn-danger');
                        button.setAttribute('type', 'button');
                        button.setAttribute('id', 'disable');
                        button.setAttribute('value', 'Disable');
                        var table = document.getElementById("roomsTable");
                        var row = table.insertRow(-1);
                        var cell1 = row.insertCell(0);
                        var cell2 = row.insertCell(1);
                        var cell3 = row.insertCell(2);
                        cell1.innerHTML = data['name'];
                        cell2.innerHTML = data['capacity']['normal'];
                        cell3.appendChild(button);
                        alert("Room" + data['name'] + "added!!");
                    }
                }else {
                    var selectList = document.createElement("select");
                    selectList.id = campus_id;
                    selectList.classList = "form-control";
                    myDiv.appendChild(selectList);
                    var option2 = document.createElement("option");
                    console.log(data['containedSpaces']);
                    option2.text = data['containedSpaces'][0].type;
                    selectList.appendChild(option2);
                    $.each(data['containedSpaces'], function (idx, item) {
                        if (item.type == "ROOM") {
                            var verification = findValue(item.name);
                            if (verification != true) {
                                roomData = getData(item.id);
                                capacity = roomData['capacity']['normal'];
                                if (capacity != 0) {
                                    var roomOption = document.createElement("option");
                                    roomOption.value = item.id;
                                    roomOption.text = item.name + '  capacity:' + capacity;
                                    selectList.appendChild(roomOption);
                                }
                            }
                        } else {
                            var option = document.createElement("option");
                            option.value = item.id;
                            option.text = item.name;
                            selectList.appendChild(option);
                        }
                    });

                }
            }
        }
    });