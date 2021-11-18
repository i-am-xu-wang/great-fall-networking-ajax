$(document).ready(function () {
    $('#submitButton').click(function () {
        confirm("Are you sure to change this user's role? ")
        var change_role_url = $(this).siblings('#role-options').attr('data-ajax-url');
        var user_id =  $(this).siblings('#role-options').attr('data-user-id');
        var user_role = $(this).siblings('#role-options').val()
        console.log(user_id)
        console.log(user_role)
        console.log(change_role_url)
        $.ajax({
            url: change_role_url,
            data: {
                user_id: user_id,
                user_role: user_role,
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
                    alert("success")
                    var new_role = json.user_role;
                    console.log(new_role);
                    $(this).siblings().children('#user-role').text(new_role);
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
});
