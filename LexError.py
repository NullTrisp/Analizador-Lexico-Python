class LexError(Exception):
    def __init__(self, err, message="Lex Error: "):
        self.message = message + err
        super().__init__(self.message)
