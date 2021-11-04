$(document).ready(function () {
    $('.eventButton').on('click', 'img', function () {
        var event_id = $(this).parent().attr('data-event-id');
        var interaction_url = $(this).parent().attr('data-ajax-url');
        var button_name = event.target.className
        $.ajax({
            url: interaction_url,
            data: {
                event_id: event_id,
                button_name: button_name,
            },
            // Whether this is a POST or GET request
            type: "POST",
            // The type of data we expect back
            dataType: "json",
            headers: {'X-CSRFToken': csrftoken},
            context: this
        })
            .done(function (json) {
                if (json.success == 'success') {
                    var eventElement;
                    var newNumber;
                    console.log(json.button_name)
                    switch (json.button_name) {
                        case 'shareButton':
                            eventElement = $(this).parent().siblings('ul.eventInfo').children('li.attendees').children('span.shareNumber');
                            newNumber = json.share_number
                            break;
                        case 'likeButton':
                            eventElement = $(this).parent().siblings('ul.eventInfo').children('li.attendees').children('span.likeNumber');
                            newNumber = json.like_number
                            break;
                    }
                    console.log(eventElement)
                    console.log(newNumber)
                    $(eventElement).text(newNumber);
                    var successMsg = $('<p class = "click-success">Click successful</p>');
                    $(this).parent().append(successMsg);
                    $(successMsg).appendTo($(this).parent()).fadeOut('slow', function () {
                        $(this).remove();
                    })
                } else {
                    alert("Error: " + json.error)
                }
            })
            .fail(function (xhr, status, errorThrown) {
                alert("Sorry, there was a problem!");
                console.log("Error: " + errorThrown);
                console.log("Status: " + status);
                console.dir(xhr);
                console.log(event_id)
            })
    });

    // the first ajax user interaction use mouseover/mouseout events.
    // retrieve the user data from user model in database
    // add new element of user information in the feeds-additional_page.html
     var userInfo;
    $('.userImage img').mouseover(function () {
         var user_id = $(this).parent().attr('data-user-id');
         var user_url = $(this).parent().attr('data-ajax-url');
         $.ajax({
            url: user_url,
            data: {
                user_id: user_id,
            },
            // Whether this is a POST or GET request
            type: "POST",
            // The type of data we expect back
            dataType: "json",
            headers: {'X-CSRFToken': csrftoken},
            context: this
        })
            .done(function (json) {
                if (json.success === 'success') {
                    if(json.name === "Anonymous User"){
                         userInfo = $("<ul class = \"popInfo\">\n" +
                "                    <li>This user choose not to declare their information</li>\n" +
                "                </ul>")
                    }
                    else{
                         userInfo = $('<ul class = "popInfo">\n' +
                '                    <li>Age: <span id = "age">' + json.age + '</span></li>\n' +
                '                    <li>Gender: <span id = "gender">'+ json.gender + '</span></li>\n' +
                '                    <li>Interested Group: <span class = "group">'+ json.group+ '</span></li>\n' +
                '                    <li>Self-Intro:  <span class = "intro">'+ json.intro+ '</span></li>\n' +
                '                </ul>')
                    }
                    var userInfoElement = $(this).parent().siblings('div.userInfo');
                    $(userInfo).appendTo(userInfoElement).show();
                } else {
                    alert("Error: " + json.error)
                }
            })
            .fail(function (xhr, status, errorThrown) {
                alert("Sorry, there was a problem!");
                console.log("Error: " + errorThrown);
                console.log("Status: " + status);
                console.dir(xhr);
                console.log(user_id)
            })
    });

    $('.userImage img').mouseout(function () {
        $(userInfo).hide();
    });


    // the second ajax request that modify the attendees value
    // click the register button will increment number of attendees by one,
    // also disable the register button from "register" to "unregister"
    $('.register').click(function () {
        var register_url = $(this).attr('data-ajax-url');
        var event_id = $(this).siblings('.eventButton').attr('data-event-id');
        console.log(event_id)
        var buttonText = $(this).text();
         $.ajax({
            url: register_url,
            data: {
                event_id: event_id,
                button_text:buttonText
            },
            // Whether this is a POST or GET request
            type: "POST",
            // The type of data we expect back
            dataType: "json",
            headers: {'X-CSRFToken': csrftoken},
            context: this
        })
            .done(function (json) {
                if (json.success === 'success') {
                     $(this).text(json.button_name);
                      attendeeElement = $(this).siblings('ul.eventInfo').children('li.attendees').children('span.attendeesNumber');
                      $(attendeeElement).text(json.attendees);
                    var successMsg = $('<p class = "click-success">' + buttonText +' &#160 successful</p>');
                    $(this).parent().append(successMsg);
                    $(successMsg).appendTo($(this).parent()).fadeOut('slow', function () {
                        $(this).remove();
                    })
                } else {
                    alert("Error: " + json.error)
                }
            })
            .fail(function (xhr, status, errorThrown) {
                alert("Sorry, there was a problem!");
                console.log("Error: " + errorThrown);
                console.log("Status: " + status);
                console.dir(xhr);
                console.log(event_id)
            })
    });









    checkQueryString();
    $("#delete").click(function () {
        return confirm("Do you want to delete");
    });

});

//search bar implementation per Project 3 requirement
function checkQueryString() {

    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString);
    if (urlParams.has('search-topics'))
        var keyword = urlParams.get("search-topics");
    $("#search-page-title").append(keyword)
    var searchResult;
    if (keyword === 'event' || keyword === 'events') {
        searchResult = $(" <ul class=\"eventInfo\">\n" +
            "                    <li class=\"eventTitle\">Bird Watchers</li>\n" +
            "                    <li class=\"eventLocation\">Location: Trail A</li>\n" +
            "                    <li class=\"eventTime\">09/01/2021 10:00 AM</li>\n" +
            "                    <li class=\"attendees\">3 attendees</li>\n" +
            "                </ul>" +
            "<ul class=\"eventInfo\">\n" +
            "                    <li class=\"eventTitle\">Music in the Woods</li>\n" +
            "                    <li class=\"eventLocation\">Location: Trail B</li>\n" +
            "                    <li class=\"eventTime\">09/11/2021 10:00 AM</li>\n" +
            "                    <li class=\"attendees\">13 attendees</li>\n" +
            "                </ul>" +
            "                <ul class=\"eventInfo\">\n" +
            "                    <li class=\"eventTitle\">Deer-patrol</li>\n" +
            "                    <li class=\"eventLocation\">Location: Trail C</li>\n" +
            "                    <li class=\"eventTime\">09/21/2021 10:00 AM</li>\n" +
            "                    <li class=\"attendees\">23 attendees</li>\n" +
            "                </ul>\n")
    } else if (keyword === "bird" || keyword === "bird watcher") {
        searchResult = $(" <ul class=\"eventInfo\">\n" +
            "                    <li class=\"eventTitle\">Bird Watchers</li>\n" +
            "                    <li class=\"eventLocation\">Location: Trail A</li>\n" +
            "                    <li class=\"eventTime\">09/01/2021 10:00 AM</li>\n" +
            "                    <li class=\"attendees\">3 attendees</li>\n" +
            "                </ul>")
    } else {
        //when input not designated phase, displaying the error message.
        searchResult = $("<h3>There is no available result.</h3>")
    }
    $(searchResult).appendTo($("div#search-result"));

}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

