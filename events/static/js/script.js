$(document).ready(function () {
    //event delegation implementation for share/like button
    // $('.eventButton').on('click', 'img', function () {
    //     event.preventDefault();
    //     var target = event.target;
    //     var eventElement;
    //     switch (target.className) {
    //         case 'shareButton':
    //             eventElement = $(this).parent().siblings('ul.eventInfo').children('li.attendees').children('span.shareNumber');
    //             break;
    //         case 'likeButton':
    //             eventElement = $(this).parent().siblings('ul.eventInfo').children('li.attendees').children('span.likeNumber');
    //             break;
    //     }
    //     var eventNumber = parseInt($(eventElement).text());
    //     eventNumber++;
    //     console.log(eventNumber);
    //     $(eventElement).text(eventNumber);
    //     var successMsg = $('<p class = "click-success">Click successful</p>');
    //     // $(this).parent().append(successMsg);
    //     $(successMsg).appendTo($(this).parent()).fadeOut('slow', function () {
    //         $(this).remove();
    //     })
    //
    // });
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

    //the second user interaction use mouseover/mouseout events.
    // add new element of user information in the feeds-additional_page.html
    var userInfo;
    $('.userImage img').mouseover(function () {
        event.preventDefault();
        var target = event.target;
        var eventElement;
        if (target.className == "heartsQueen") {
            userInfo = $('<ul class = "popInfo">\n' +
                '                    <li>Age: 27</li>\n' +
                '                    <li>Gender: Female</li>\n' +
                '                    <li>Interested Group: Bird Watchers</li>\n' +
                '                    <li>Self-Intro: I am Hearts Queen. Nice to meet you</li>\n' +
                '                </ul>')
        } else {
            userInfo = $("<ul class = \"popInfo\">\n" +
                "                    <li>This user choose not to declare their information</li>\n" +
                "                </ul>")
        }
        userInfoElement = $(this).parent().siblings('div.userInfo');
        $(userInfo).appendTo(userInfoElement).show();
    });
    $('.userImage img').mouseout(function () {
        $(userInfo).hide();
    });


    // register and unregister button, the number of attendee will add/minus respectively
    $('.register').click(function () {
        attendeeElement = $(this).siblings('ul.eventInfo').children('li.attendees').children('span.attendeesNumber');
        var attendeeNumber = parseInt($(attendeeElement).text());
        console.log($(this).text());
        if ($(this).text() == "Register") {
            $(this).text("Unregister");
            attendeeNumber++;
        } else {
            $(this).text("Register");
            attendeeNumber--;
        }
        $(attendeeElement).text(attendeeNumber);
    });

    $("#delete").click(function () {
        return confirm("Do you want to delete");
    });

    checkQueryString();


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

