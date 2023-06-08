class User:
    def __init__(self, Username, Password, Email, Points, Created):
        self.Username = Username
        self.Password = Password
        self.Email = Email
        self.Points = Points
        self.Created = Created


    def __repr__(self):
        return "User('{}', '{}', '{}', {}, {})".format(self.Username, self.Password, self.Email, self.Points, self.Created)