window.onload = function () {
    $('.basket_table').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
        console.log(t_href.name)
        console.log(t_href.value)
        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                $('.basket_table').html(data.result);
            },

        });
        event.preventDefault();
    });
}