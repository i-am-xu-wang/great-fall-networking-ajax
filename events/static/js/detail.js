// $(document).ready(function () {
//     //sorted button on the events list page
//
//     $('#createEvent').on('click', 'submit', function () {
//         var event_id = $(this).parent().attr('data-event-id');
//         var event_add_url = $(this).parent().attr('data-ajax-url');
//         $.ajax({
//             url: events_add_url,
//             data: {
//                event_id:event_id,
//             },
//             // Whether this is a POST or GET request
//             type: "POST",
//             // The type of data we expect back
//            // dataType: "json",
//             headers: {'X-CSRFToken': csrftoken},
//             context: this
//         })
//             .done(function (json) {
//                 alert("ajax successful")
//             })
//             .fail(function (xhr, status, errorThrown) {
//                 alert("Sorry, there was a problem!");
//                 console.log("Error: " + errorThrown);
//                 console.log("Status: " + status);
//                 console.dir(xhr);
//             })
//
//     });
//
//     });
//
//
// });