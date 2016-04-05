var socket = io.connect('http://' + document.domain + ':' + location.port + '/core');
var gameChoose = '';


function sendSocket(emitName, obj) {
    socket.emit(emitName, obj);
}

sendSocket('joining', {rooms: ['klark-room']});

socket.on('game-created', function (data) {
    Advertise(data);
});

socket.on('my-game-created', function (data) {
        sendSocket('joining', {rooms: [data.game]});
});



socket.on('load-game', function (data) {
    console.log(data);
    console.log('loading-game');
    // if (gameChoose = data['game']) {
        setTimeout(function () {
            window.location.href = 'http://' + document.domain + ':' + location.port + '/' + data['game']
        }, 1000);
    // }
});


function Advertise(context) {
    console.log('Advertise');
    var trAttr = '.wall-games>tbody>tr';
    var idElement = $(trAttr).last();
    idElement = parseInt(idElement.attr('id')) + 1;
    
    $('.wall-games>tbody').append(
        "<tr id='" + idElement + "'>" + context.template + "</tr>"
    );
}

$('.out-a>.in-a').on('click', function () {
    var data = {
        'nickname': $('#nickname').val(),
        'q': $('#q-to-win').val(),
        'size': $('#g-b-size').val(),
        'v': $('input[name=ch-v]')[0].checked,
        'h': $('input[name=ch-h]')[0].checked,
        'd': $('input[name=ch-d]')[0].checked
    };

    console.log('create-game');
    console.log(data);
    sendSocket('create-game', data);

});

function startPlay(event) {
    console.log('start preparing');
    var parentId = event.target.parentNode.id;
    var children = $('#' + parentId).children('td');
    var nickname = $('#nickname').val();
    var data = {
        'game' : children[1].innerHTML,
        'nickname': nickname
    };

    sendSocket('joining', {rooms: [data.game]});
    setTimeout(function () {
        sendSocket('prepare-game', data);
    }, 2000)
}
