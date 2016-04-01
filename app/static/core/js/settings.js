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