from flask import abort


def check_game(game):
    if len(game) != 8:
        abort(404)

    try:
        game = int(game)
    except ValueError:
        abort(403)


