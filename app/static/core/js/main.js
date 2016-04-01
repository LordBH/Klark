/**
 * Created by lordbh on 3/30/16.
 */

$(function () {
    var list = $('input[type=range]');
    for (var i = 0; i < list.length; i++) {
        var idElement = '#' + list[i].id;
        var inputText = $(idElement).next('input[type=text]')[0];
        inputText.value = $(idElement)[0].value;
    }
});

$('input[type=range]').on('mousemove', function (d) {
    var idElement = '#' + d.target.id;
    var inputText = $(idElement).next('input[type=text]')[0];
    inputText.value = $(idElement)[0].value;
});


$('li>a').click(function (event) {
    event.preventDefault();
    var c_name = event.currentTarget.id;
    var attributeTop = $('#' + c_name).offset().top;
    $('.arrow-menu').css({
        'top': attributeTop - 22,
        'transition': 'top .5s'
    });
});
