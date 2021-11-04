$(document).ready(function () {
    //sorted button on the events list page

    $('#side-tabs').on('click', 'li', function () {
        var events_list_url = $(this).parent().attr('data-ajax-url');
        var button_name = event.target.className
        console.log(events_list_url)
        console.log(button_name)
        $.ajax({
            url: events_list_url,
            data: {
               button_name: button_name,
            },
            // Whether this is a POST or GET request
            type: "POST",
            // The type of data we expect back
           // dataType: "json",
            headers: {'X-CSRFToken': csrftoken},
            context: this
        })
            .done(function (json) {
                alert("ajax successful")
            })
            .fail(function (xhr, status, errorThrown) {
                alert("Sorry, there was a problem!");
                console.log("Error: " + errorThrown);
                console.log("Status: " + status);
                console.dir(xhr);
            })

    });


});