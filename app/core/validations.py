from werkzeug.utils import secure_filename


class ValidateConfig:
    FAIL = False

    def __call__(self, data):

        data['nickname'] = self.valid_nickname(data['nickname'])
        data['rules'] = self.valid_rules(data['rules'])

        self.valid_size(data['q_count'])
        self.valid_size(data['q_size'])
        self.valid_colors(data['colors'])
        self.valid_symbols(data['symbols'])

        if self.FAIL:
            return False
        return True

    def valid_nickname(self, q):
        if len(q) < 2:
            self.FAIL = True
        return secure_filename(q)

    def valid_size(self, q):
        try:
            q = int(q)
            if not (2 < q < 13):
                self.FAIL = True
        except ValueError:
            self.FAIL = True

    def valid_rules(self, q):
        for x in q:
            x = x[0]
            if x not in ['v', 'h', 'd']:
                self.FAIL = True
        return q

    def valid_colors(self, q):
        for x, y in q.items():
            for i in y:
                try:
                    i = int(i)
                except ValueError:
                    self.FAIL = True
                if not (0 <= i <= 255):
                    self.FAIL = True

            if x[0] not in ['f', 's', 'n', 'c']:
                self.FAIL = True

    def valid_symbols(self, q):
        for x in q:
            if len(x) != 1:
                self.FAIL = True
