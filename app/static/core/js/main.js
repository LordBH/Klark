var boardRangeSize = 0;
var maxSize = 0;
var boardSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'];


$(function () {
    var list = $('input[type=range]');
    var al = $('#alert');

    if (al.text() != '') {
        al.addClass('s-a');
        setTimeout(function () {
            al.removeClass('s-a');
        }, 7000)
    }

    for (var i = 0; i < list.length; i++) {
        var idElement = '#' + list[i].id;
        var inputText = $(idElement).next('input[type=text]')[0];
        inputText.value = $(idElement)[0].value;
    }

    idElement = '#g-b-size';
    boardRangeSize = $(idElement)[0].value;
    maxSize = $(idElement)[0].max;
    createBoard(maxSize);
    changeViewBoardSize(boardRangeSize);


    var s1 = $('#noughts-').val();
    var s2 = $('#crosses-').val();
    $('#a1').text(s1);
    $('#a2').text(s2);
    $('#b1').text(s1);
    $('#b2').text(s2);
    
    $('.board-color>div>input[type=range]').trigger('input');

});

$('input[type=text]').on('change', function (d) {
    var idElement = '#' + d.target.id;
    var inputText = $(idElement).prev('input[type="range"]');
    var v = $(idElement).val();
    inputText.val(v);
    $('.board-color>div>input[type=range]').trigger('input')
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


$('.board-color>div>input[type=range]').on('input', function (d) {

    var idElement = '#' + d.target.id;
    var classID = idElement[idElement.length - 1];
    var c_rgb = $('.' + classID + '-color>input[type=range]');
    var rgb = '#';

    for (var i = 0; i < c_rgb.length; i++) {
        var val = c_rgb[i].value;
        val = checkInterval(val);
        rgb += val
    }
    console.log(rgb);

    if (classID == 'f') {
        $('.' + 'blc').not('.dsp-none').css('background-color', rgb)
    }
    else if (classID == 's') {
        $('.' + 'wht').not('.dsp-none').css('background-color', rgb);
    } else if (classID == 'n') {
        $('.' + 'blc').not('.dsp-none').css('color', rgb);
    } else if (classID == 'c') {
        $('.' + 'wht').not('.dsp-none').css('color', rgb);
    }
});


$('.symbol-f').on('keyup', function (e) {
    var idElement = '#' + e.target.id;
    var v = $(idElement).val().toUpperCase();

    if (idElement == '#crosses-') {
        $('#a2').text(v);
        $('#b2').text(v);

    } else if (idElement == '#noughts-') {
        $('#a1').text(v);
        $('#b1').text(v);
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
    $('.' + c).css('visibility', 'visible');
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

    if (wrapper.children().hasClass('cont-f')) {
        wrapper.children().css('visibility', 'hidden');
    }

    wrapper.removeClass(show);
    $('.' + ch).parent().addClass(show);
}

function sendRecall() {
    var v1 = $('#title-').val();
    var v2 = $('#msg').val();
    if (v1.length > 2 && v2.length > 5) {
        $('#re-call').submit();
    } else {
        alertMessage("Please type more information to title or message");
    }
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
            } else {
                $(bor).append('<div id="' + boardSymbols[y] + i + '" class="dsp-none ' + black + '"></div>');
            }
            if (val == i) {
                var extra = black;
                black = white;
                white = extra;
            }
        }
}

function changeViewBoardSize(val) {
    var v = parseInt(val);
    var b_d = '.bor>div';

    $(b_d).css({
        'flex-grow': v,
        'flex-basis': 100 / v + '%',
        'width': 650 / (v * v),
        'height': 650 / v
    });

    if (v == 3) {
        $(b_d).css('font-size', (650 / v) - v * 12);
    } else if (v < 6) {
        $(b_d).css('font-size', (650 / v) - v * 3);
    } else if (v < 10) {
        $(b_d).css('font-size', (650 / v) - v * 2);
    } else {
        $(b_d).css('font-size', (650 / v) - v);
    }


    for (var i = 0; i < maxSize; i++)
        for (var j = 1; j < maxSize + 1; j++) {
            if (j < v + 1 && i < v)
                $('#' + boardSymbols[i] + j).removeClass('dsp-none');
            else
                $('#' + boardSymbols[i] + j).addClass('dsp-none');
        }
}


function checkInterval(value) {
    var v = parseInt(value);
    if (v > 255) {
        return 'ff'
    } else if (v < 0) {
        return '00'
    } else {
        var s = v.toString(16);
        if (s.length != 2) {
            s = 0 + s
        }
        return s
    }
}

function alertMessage(msg) {
    var al = '#alert';
    $(al).text(msg);
    $(al).addClass('s-a');
    setTimeout(function () {
        $(al).removeClass('s-a');
    }, 7000)
}