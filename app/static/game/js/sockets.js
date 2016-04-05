var socket = io.connect('http://' + document.domain + ':' + location.port + '/core');


function sendSocket(emitName, obj) {
    socket.emit(emitName, obj);
}

socket.on('players', function (number) {
    console.log('join', number);
    $('.watch').text(number);
});

socket.on('show-message', function (data) {
    console.log('show-message', data);
    var addHTML = '<div class="message"><div class="nickname">';
    addHTML += data.nickname +  '</div><div class="text">' + data.msg + '</div></div>';
    $('.log').append(addHTML);
});


socket.on('show-symbol', function (data) {
    console.log('show-symbol', data);
    var elementID = '#' + data.id;

    if (data.symbol){
        $(elementID).css('color', colorCrossesCell);
        $(elementID).text(crosses);
    }else{
        $(elementID).css('color', colorNoughtsCell);
        $(elementID).text(noughts);
    }

});