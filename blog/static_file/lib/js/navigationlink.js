var url = $(location).attr('href');
var abs_url = url.split('#')[1];
abs_url = '#' + abs_url;

$('#navmenu li a').each(function () {

    if ($(this).attr('href') == abs_url) {

        $(this).closest('li').addClass('active');
    }
    else {
        $(this).closest('li').removeClass('active');
    }
    $('#category_menu li.active').removeClass('active');

});















