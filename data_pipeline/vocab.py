class Vocabulary:
    def __init__(self, tokens=None):
        self.token_to_id = {}
        self.id_to_token = []

        for token in tokens or []:
            self.add_token(token)

    def add_token(self, token):
        if not isinstance(token, str):
            raise TypeError('token must be a string')

        if token not in self.token_to_id:
            token_id = len(self.id_to_token)
            self.token_to_id[token] = token_id
            self.id_to_token.append(token)

        return self.token_to_id[token]

    def get_id(self, token):
        return self.token_to_id[token]

    def get_token(self, token_id):
        if not isinstance(token_id, int) or isinstance(token_id, bool):
            raise TypeError('token_id must be an integer')

        if token_id < 0 or token_id >= len(self.id_to_token):
            raise IndexError('token ID out of range')

        return self.id_to_token[token_id]

    def encode(self, tokens):
        return [self.get_id(token) for token in tokens]

    def decode(self, token_ids):
        return [self.get_token(token_id) for token_id in token_ids]

    def __contains__(self, token):
        return token in self.token_to_id

    def __len__(self):
        return len(self.id_to_token)
