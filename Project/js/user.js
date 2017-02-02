/**
 * Created by carloscosta on 27-12-2016.
 */
$(document).ready(function () {
    var username = document.getElementById('username').innerHTML;
    var identifier = document.getElementById('identifier').innerHTML;

    $('#checkTable').on('click', 'button', function(e){
            var data = $(this).closest('tr')[0];
            var room = data.cells[0].innerHTML;
            var button = data.cells[2].children[0];
            var verification = findValue();
            if (button.className == 'btn-success') {
                if (verification != true) {
                    var capacity = occupancy(room, "check-in");
                    console.log(capacity);
                     if(capacity == 0){
                        alert("ROOM IS FULL");
                     }else {
                         button.className = 'btn-danger';
                         button.innerHTML = 'Check-out';
                         check_in(username, identifier, room, "true");
                         data.cells[1].innerHTML = capacity;
                     }
                } else {
                    alert("CHECK-OUT FIRST BEFORE GO TO ANOTHER ROOM!")
                }
            } else {
                check_out(identifier);
                button.className = 'btn-success';
                button.innerHTML = 'Check-in';
                data.cells[1].innerHTML = occupancy(room, "check-out");
            }
    });

    $('#checkTable').on('click', 'input', function(e){
        var data = $(this).closest('tr')[0];
        var room = data.cells[0].innerHTML;
        var myDiv = document.getElementById(room);
        var who = who_is_in_the_room(room);
        document.getElementById(room).style.display = "inline-block";
        var selectList = document.createElement("select");
                selectList.classList = "form-control";
                myDiv.appendChild(selectList);
        var option1 = document.createElement("option");
        if(who.length == 0){
            option1.text = "--NONE--";
            selectList.appendChild(option1);
        }else {
            option1.text = "--SEE--";
            selectList.appendChild(option1);
            $.each(who, function (idx, item) {
                var option = document.createElement("option");
                option.text = item;
                selectList.appendChild(option);
            });
        }
    });

    function occupancy(room, check){
        var capacity;
        $.ajax({
                        type: "POST",
                        async: false,
                        url: "/occupancy/" + room + "/" + check,
                        success: function(response){
                                capacity = response;
                            console.log(response);
                        }
                 });
        return capacity;
    }

    function findValue(){
            var table = document.getElementById('checkTable');
            for(var i=1;i<table.rows.length;i++) {
                var trs = table.getElementsByTagName("tr")[i];
                var cellVal = trs.cells[2].children[0].className;
                if(cellVal == 'btn-danger' ){
                    return true
                }
            }
            return false

        }

    function check_in(user, id, room, checkin) {

                    $.ajax({
                        type: "POST",
                        async: false,
                        url: "/checkin/" + user + "/" + id + "/" + room + "/" + checkin,
                        success: function(response){
                                alert(response);
                        }
                 });
                }

    function check_out(id) {
                    $.ajax({
                        type: "POST",
                        async: false,
                        url: "/checkout/" + id,
                        success: function(response){
                                alert(response);
                        }
                 });
                }

    function who_is_in_the_room(room) {
        var data;
                    $.ajax({
                        type: "GET",
                        async: false,
                        url: "/who_is_in_the_room/" + room,
                        success: function(response){
                            if(response == "None"){
                                data = "None"
                            }else{
                                data = JSON.parse(response);
                            }
                        }
                 });
        return data
                }


});