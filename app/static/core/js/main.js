/**
 * Created by lordbh on 3/30/16.
 */

$(function () {
    var list = $('input[type=range]');
    var alert = $('.alert');
    for (var i = 0; i < list.length; i++) {
        var idElement = '#' + list[i].id;
        var inputText = $(idElement).next('input[type=text]')[0];
        inputText.value = $(idElement)[0].value;
    }
    if (alert[0].innerHTML){
        alert.addClass('s-a');
        setTimeout(function () {
            alert.removeClass('s-a');
        }, 7000)
    }


});

$('input[type=range]').on('mousemove', function (d) {
    var idElement = '#' + d.target.id;
    var inputText = $(idElement).next('input[type=text]')[0];
    inputText.value = $(idElement)[0].value;
});


$('li').click(function (event) {
    event.preventDefault();
    var c_name = event.currentTarget.id;
    var attributeTop = $('#' + c_name).offset().top;
    $('.arrow-menu').css({
        'top': attributeTop - 22,
        'transition': 'top .5s'
    });
    ChangeFixedWrapper(c_name)
});

function ChangeFixedWrapper(id) {
    if (id == 'games') {
        showGames()
    } else if (id == 'sett') {
        showSettings()
    }
}
function showGames() {
    var c = 'board';
    changeView(c);
}

function showSettings() {
    var c = 'set-board';
    changeView(c);
}
function showContacts() {
    var c = 'cont-f';
    changeView(c);
}

function changeView(ch) {
    var show = 'show-div';
    var wrapper = $('.' + show);

    wrapper.removeClass(show);
    $('.' + ch).parent().addClass(show);
}

function sendRecall(){
    $('#re-call').submit();
}