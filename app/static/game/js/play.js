var gameID = '';
var boardRangeSize = parseInt($('#s-board').text());
var quantityToWin = $('.q-t').text();
var colorFirstCell = $('#first-clr').text();
var colorSecondCell = $('#second-clr').text();
var colorNoughtsCell = $('#noughts-clr').text();
var colorCrossesCell = $('#crosses-clr').text();
var symbolID = '#symbols';
var noughts = $(symbolID).text()[0];
var crosses = $(symbolID).text()[2];
var firstMove = $('#beginMoving').text();
var boardSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'];
var symbol = 'X';
var FLAG = true;

$(document).ready(function () {
    createBoard(boardRangeSize);
    changeViewBoardSize(boardRangeSize);
    $('.blc').css('background-color', colorFirstCell);
    $('.wht').css('background-color', colorSecondCell);

    gameID = $('#link').attr('value');
    gameID = gameID.split('/');
    gameID = gameID[gameID.length - 1];
    sendSocket('game-on', {rooms: gameID});

    if (firstMove == 'True') {
        firstMove = true;
        symbol = crosses;
        alert('U move bitch first');
    } else {
        firstMove = false;
        FLAG = false;
        symbol = noughts
    }
    $('#c-msg').focus();
});

    function createBoard(val) {
        var bor = '.bor';
        var black = 'blc';
        var white = 'wht';
        var v = parseInt(val);

        for (var y = 0; y < v; y++)
            for (var i = 1; i < v + 1; i++) {
                var beginDiv = '<div id="' + boardSymbols[y] + i + '" class="';
                var endDiv = '" onclick="setSymbol(event)"></div>';

                if (i % 2 == 0) {
                    $(bor).append(beginDiv + white + endDiv);
                } else {
                    $(bor).append(beginDiv + black + endDiv);
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
}

function setSymbol(event) {
    if (firstMove) {
        firstMove = false;
        event.target.innerHTML = symbol;
        var val = true;
        if (symbol == noughts) {
            val = false
        }
        sendSocket('symbol-set', {id: event.target.id, symbol: val, room: gameID})
    }
}


$('#c-msg').keypress(function (event) {
    if (event.keyCode == (13)) {
        event.preventDefault();
        sendMessage();
    }

});
$('.d-but-3').click(function (event) {
    sendMessage();
});

function sendMessage() {
    console.log('sendMessage');
    var msgId = '#c-msg';
    var message = $(msgId).val();
    $(msgId).val('').focus();
    if (msgId != '') {
        console.log('send');
        sendSocket('enter-message', {msg: message, room: gameID})
    }
}
// function alertMessage(msg) {
//     var al = '#alert';
//     $(al).text(msg);
//     $(al).addClass('s-a');
//     setTimeout(function () {
//         $(al).removeClass('s-a');
//     }, 7000)
// }