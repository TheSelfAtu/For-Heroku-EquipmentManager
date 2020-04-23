$(function () {
    $('#button').bind("click", function () {
        var re_num = new RegExp($('#search_num').val());
        var re_name = new RegExp($('#search_name').val());
        var re_email = new RegExp($('#search_email').val());
        var re_department = new RegExp($('#search_department').val());
        $('#result tbody tr').each(function () {
            var txt_num = $(this).find("td:eq(0)").html();
            var txt_name = $(this).find("td:eq(1)").html();
            var txt_email = $(this).find("td:eq(2)").html();
            var txt_department = $(this).find("td:eq(3)").html();
            if (txt_num.match(re_num) != null && txt_name.match(re_name) != null && 
txt_email.match(re_email) != null && txt_department.match(re_department) != null) { 
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });

    $('#button2').bind("click", function () {
        $('#search').val('');
        $('#result tr').show();
    });
});