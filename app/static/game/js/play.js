var boardRangeSize = 12;
var maxSize = 0;
var boardSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'];
var symbol = 'X';


$(function () {
    createBoard(boardRangeSize);
    changeViewBoardSize(boardRangeSize);
});

function createBoard(val) {
    var bor = '.bor';
    var black = 'blc';
    var white = 'wht';
    var v = parseInt(val);

    for (var y = 0; y < v; y++)
        for (var i = 1; i < v + 1; i++) {
            var beginDiv = '<div id="' + boardSymbols[y] + i + '" class="';
            var endDiv  = '" onclick="setSymbol(event)"></div>';

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


    for (var i = 0; i < maxSize; i++)
        for (var j = 1; j < maxSize + 1; j++) {
            if (j < v + 1 && i < v)
                $('#' + boardSymbols[i] + j).removeClass('dsp-none');
            else
                $('#' + boardSymbols[i] + j).addClass('dsp-none');
        }
}

function setSymbol(event) {
    event.target.innerHTML = symbol;
    console.log(event)
}


// function alertMessage(msg) {
//     var al = '#alert';
//     $(al).text(msg);
//     $(al).addClass('s-a');
//     setTimeout(function () {
//         $(al).removeClass('s-a');
//     }, 7000)
// }