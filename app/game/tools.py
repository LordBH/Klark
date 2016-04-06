from app.models import UserConfigurations, db
from app.core.tools import get_colors
from flask import abort, request, session
from random import choice


GAME_CONTEXT_CHECKER = {}
boardSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']


def create_template(q):
    game = q.game_id
    opponent = q.player1
    board_size = q.q_size
    quantity = q.q_count
    rules = ''
    for y in q.rules.split('|')[:-1]:
        rules += y.upper() + ' '
    butt = """<td class="start-play" onclick="startPlay(event)">Play</td>"""

    template = ''

    for x in [game, opponent, board_size, quantity, rules]:
        template += "<td>" + str(x) + "</td>"

    template += butt

    return template


def check_game(game):
    if len(game) != 8:
        abort(404)
    try:
        int(game)
    except ValueError:
        abort(404)


def set_player(q, pl):
    ip = request.remote_addr

    q.player2 = pl
    q.ip2 = ip

    db.session.add(q)
    db.session.commit()


def create_context_game(query):
    context = {
        'link': 'http://' + request.host + '/' + query.game_id,
        'moves': 0,
        'quantity': query.q_count,
        'size': query.q_size,
        'player1': query.player1,
        'player2': query.player2,
        'rules': {}
    }

    GAME_CONTEXT_CHECKER.setdefault(query.game_id, {
        'count': 0,
        'flag': choice([True, False])
    })

    game_id = GAME_CONTEXT_CHECKER[query.game_id]

    if game_id['count'] == 0:
        context['flag'] = game_id['flag']
    elif game_id['count'] == 1:
        context['flag'] = not game_id['flag']

    game_id['count'] += 1

    for x in query.rules.split('|')[:-1]:
        val = False
        if x:
            val = True
        context['rules'][x.upper()] = val
    if session.get('nickname') != 'Guest':
        get_user_settings(context)

    return context


def get_user_settings(cont):
    q = UserConfigurations.query.filter_by(ip=request.remote_addr).first()
    if q is not None:
        col = get_colors(q.__dict__)['colors']
        for y in col:
            cont[y] = '#'
            for x in ['r', 'g', 'b']:
                s = hex(int(col[y][x]))[2:]
                if len(s) != 2:
                    s = '0' + s
                cont[y] += s
        cont['symbols'] = q.symbols


def check_location(i, ex, flag):
    row, col = i[0], int(i[1:]) - 1
    f = [check_horizontal, check_vertical, check_diagonal]
    rul = ex['rules']
    m = ex['moves']
    size = len(m[row])
    val = 0
    if flag:
        val = 1

    m[row][col] = val

    for func, x in zip(f, rul):  # horizontal, vertical, diagonal

        if x is not None:
            response = func(row, col, m, val, size, int(ex['q']))
            print()
            print(response)
            print()
            if response:
                return flag

    return -1


def check_horizontal(row, col, cont, val, size, q):
    start = 1
    for inx in range(1, size + 1):
        cell = cont[row][inx - 1]

        if cell == val:
            if inx - start == q:
                return True
        else:
            start = inx


def check_vertical(row, col, cont, val, size, q):
    start = 0
    for inx, key in zip(range(size), boardSymbols):
        cell = cont[key]
        print(cell, row, inx)
        if cell[col] == val:
            print('start', cell, row, q, inx, start, inx - start)
            print('start', type(cell), type(row), type(inx), type(q), type(inx - start + 1))
            if inx - start + 1 == q:
                return True
        else:
            start = inx + 1


def check_diagonal(row, col, cont, val, size, q):
    board, row = create_new_board(cont, size, row)

    subtract = abs(row - col)

    start = 0

    row1, col1 = get_row1_and_col1(row, col, subtract)
    row2, col2, count = get_row2_and_col2(row, col, size)
    print()
    print(row1, col1)
    print(row2, col2, count)
    print()

    for x in range(size - subtract):
        cell = board[row1 + x][col1 + x]

        if cell == val:
            if x - start + 1 == q:
                return True
        else:
            start = x + 1

    for x in range(count):
        print(row2)
        print(x)
        cell = board[row2 - x][col2 + x]

        if cell == val:
            if x - start + 1 == q:
                return True
        else:
            start = x + 1


def create_new_board(location, size, row):
    extra = {}
    for inx, sym in zip(range(size), boardSymbols):
        extra[inx] = location[sym]
        if row == sym:
            row = inx
    return extra, row


def get_row1_and_col1(row, col, subtract):
    if row > col:
        print('row1>col1')
        row1 = subtract
        col1 = 0

    elif row == col:
        print('r1=w1')
        row1 = col1 = 0
    else:
        print('row1<col1')
        row1 = 0
        col1 = subtract

    return row1, col1


def get_row2_and_col2(row, col, size):
    print(row, col, size)
    row = size - row - 1
    if row > col:
        print('row2>col2')
        row2 = row - col
        col2 = 0
        s = size - row2
    elif size - 1 == row + col:
        print('r2=w2')
        row2 = col2 = size - 1
        s = size
    else:
        print('row2<col2')
        row2 = 0
        col2 = col - row
        s = size - col2
    print(size - row2 - 1, col2, s)
    return size - row2 - 1, col2, s
