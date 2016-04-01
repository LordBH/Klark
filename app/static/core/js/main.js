/**
 * Created by lordbh on 3/30/16.
 */

var boardRangeSize = 0;
var maxSize = 0;
var boardSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'];

$(function () {
    var list = $('input[type=range]');
    var alert = $('#alert');
    for (var i = 0; i < list.length; i++) {
        var idElement = '#' + list[i].id;
        var inputText = $(idElement).next('input[type=text]')[0];
        inputText.value = $(idElement)[0].value;

        if (idElement == '#g-b-size') {
            boardRangeSize = $(idElement)[0].value;
            maxSize = $(idElement)[0].max;
            createBoard(maxSize);
            changeViewBoardSize(boardRangeSize);

        }
    }
    if (alert[0]) {
        alert.addClass('s-a');
        setTimeout(function () {
            alert.removeClass('s-a');
        }, 7000)
    }


});

$('input[type=range]').on('mousemove', function (d) {
    var idElement = '#' + d.target.id;
    var inputText = $(idElement).next('input[type=text]')[0];
    var val = $(idElement)[0].value;
    inputText.value = val;

    if (idElement == '#g-b-size' && boardRangeSize != val) {
        boardRangeSize = val;
        changeViewBoardSize(val)
    }
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
    var b = 'set-board';
    changeView(b);


    var hr = '.hor-set';
    $('.wrapper').css('height', 1900);
    $(hr).removeClass('no-animate-set');
    $(hr).addClass('animate-set');
    //
    var config = '.config';
    $(config).show();
    $(config).removeClass('no-animate-set');
    $(config).addClass('animate-set');

}
function showContacts() {
    var c = 'cont-f';
    changeView(c);
}

function changeView(ch) {
    var show = 'show-div';
    var wrapper = $('.' + show);
    if (wrapper.children().hasClass('set-board')) {
        var hr = '.hor-set';
        $('.wrapper').css('height', '100%');
        $(hr).removeClass('animate-set');
        $(hr).addClass('no-animate-set');

        var config = '.config';
        $(config).addClass('no-animate-set');
        $(config).removeClass('animate-set');
        $(config).hide();
    }

    wrapper.removeClass(show);
    $('.' + ch).parent().addClass(show);
}

function sendRecall() {
    $('#re-call').submit();
}

function saveSettings() {
    $('#settings').submit();
}

function createBoard(val) {
    var bor = '.bor';
    var black = 'blc';
    var white = 'wht';
    var v = parseInt(val);

    for (var y = 0; y < v; y++)
        for (var i = 1; i < v + 1; i++) {
            if (i % 2 == 0) {
                $(bor).append('<div id="' + boardSymbols[y] + i + '" class="dsp-none ' + white + '"></div>');
                if (v % 2 == 0 && val == i) {
                    var extra = black;
                    black = white;
                    white = extra;
                }
            } else {
                $(bor).append('<div id="' + boardSymbols[y] + i + '" class="dsp-none ' + black + '"></div>');
            }
        }
}

function changeViewBoardSize(val) {
    var v = parseInt(val);
    $('.bor>div').css({
       'flex-grow': v,
       'flex-basis': 100/v + '%',
        'width': 650/(v*v),
        'height': 650/v
    });

    for (var i = 0; i < maxSize; i++)
        for (var j = 1; j < maxSize + 1; j++) {
            if (j < v + 1 && i < v)
                $('#' + boardSymbols[i] + j).removeClass('dsp-none');
            else
                $('#' + boardSymbols[i] + j).addClass('dsp-none');
}

}