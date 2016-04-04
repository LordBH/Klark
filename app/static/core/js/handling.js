var socket = io.connect('http://' + document.domain + ':' + location.port + '/core');
var game = 0;
var change = '';

sendSocket('join-rooms');

function sendSocket(emitName, obj) {
    socket.emit(emitName, obj);

}

socket.on('game-created', function (data) {
    Advertise(data);
    change = data['game'];
});

socket.on('load-game', function (data) {
    console.log(data);
    console.log('start');
    setTimeout(function () {
        window.location.href = 'http://127.0.0.1:5000/' + change
    }, 5000);
});

$('.out-a>.in-a').on('click', function () {
    var data = {
        'nickname': $('#nickname').val(),
        'q': $('#q-to-win').val(),
        'size': $('#g-b-size').val(),
        'v': $('input[name=ch-v]')[0].checked,
        'h': $('input[name=ch-h]')[0].checked,
        'd': $('input[name=ch-d]')[0].checked
    };

    console.log(data);
    sendSocket('create-game', data);

});


// $('.out-a>.in-f').on('click', function (){
//     var data = {
//         'nickname': $('#nickname').val(),
//         'q': $('#q-to-win').val(),
//         'size': $('#g-b-size').val(),
//         'v': $('input[name=ch-v]').val(),
//         'h': $('input[name=ch-h]').val(),
//         'd': $('input[name=ch-d]').val()
//     };
//
//     sendSocket('create-game', data);
//
// });


function Advertise(context) {
    alertMessage(context);
    sendSocket('prepare-game', {'game': context['game']});
    console.log(context);
}

