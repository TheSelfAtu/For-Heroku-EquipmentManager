$(function(){
    $('#button').bind("click",function(){
    var re_num = new RegExp($('#search_num').val());
    var re_cg = new RegExp($('#search_category').val());
    var re_ld = new RegExp($('#search_loaned').val());
            $('#result tbody tr').each(function(){
        var txt_num = $(this).find("td:eq(0)").html();
        var txt_cg = $(this).find("td:eq(2)").html();
                    var txt_ld = $(this).find("td:eq(4)").html();
                    if(txt_num.match(re_num) != null && txt_cg.match(re_cg) != null && txt_ld.match(re_ld) != null  ){
                            $(this).show();
                    }else{
                            $(this).hide();
                    }
            });
    });

    $('#button2').bind("click",function(){
            $('#search').val('');
            $('#result tr').show();
    });
});