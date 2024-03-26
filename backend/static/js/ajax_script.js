$(document).ready(function () {
    function updateRandomNumber() {
        $.ajax({
            url: window.location.href,
            type: 'GET',
            success: function (data) {
                let number = $(data).find('#random_number').text();
                $('#random_number').text(number);
            },
        });
    }

    setInterval(updateRandomNumber, 1000);
});