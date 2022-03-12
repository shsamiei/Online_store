


class User :
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.info = {'user' : self.username , 'pass' : self.password}
        self.bouthList = []
        pass

