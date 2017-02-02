/**
 * Created by carloscosta on 26-12-2016.
 */

$(document).ready(function () {
    document.getElementById("register").onclick = function () {
            var username = document.getElementById("username").value;
            register(username);
        };

    document.getElementById("login").onclick = function () {
            var identifier = document.getElementById("identifier").value;
            login(identifier);
        };

    function register(username) {
        $.ajax({
            type: "POST",
            async: false,
            url: "/register/" + username,
            success: function(response){
                alert(response);
            }
        });
    }

    function login(identifier) {
        $.ajax({
            type: "GET",
            url: "/login/" + identifier,
            success: function(response){
                if(response == "None"){
                    alert("Identifier don't exist. Try again or register.");
                }
                if(response == "admin"){
                    window.location.href = '/admin/' + 0;
                }else
                {
                    var data = JSON.parse(response);
                    var username = data[0];
                    var identifier = data[1];
                    window.location.href = '/user/' + username + '/' + identifier;
                }

            }
        });
    }


});
