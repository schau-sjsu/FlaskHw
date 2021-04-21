from app import db

class User(db.Model):
    """
    Represent a table of users for the message board.

    Attributes
    ----------
    id : Column
        User id represented by an integer.
    author : Column
        Name of the user represented by a string.
    message : Column
        Message posted by the user represented by a string.
    """
    # have the following columns:
    # id (int)
    # Allow message table to use to link message to user
    id = db.Column(db.Integer, primary_key=True)

    # author (string, unique, can't be null)
    # Avoid ambiguity of having different authors with the same name
    author = db.Column(db.String, nullable=False, unique=True)

    # message (linkd to Messages table)
    message = db.relationship('Messages', backref='user', lazy=True)

    """
    Output name of user.
    """
    def __repr__(self):
        return f'<User {self.author}>'

class Messages(db.Model):
    """
    Represent a table of messages for the message board.

    Attributes
    ----------
    id : Column
        Message id represented by an integer.
    message : Column
        Message posted by the user represented by a string.
    user_id : Column
        Id of user who posted the message represented by an integer.
    """
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key=True)

    # message (string, not unique, can't be null)
    # Allow different users to post the same message
    message = db.Column(db.String, nullable=False, unique=False)

    # user_id link to id (int)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # write __repr__ that outputs
    # <Message: MESSAGE_GOES_HERE>
    # replace MESSAGE_GOES_HERE with the message
    """
    Output message.
    """
    def __repr__(self):
        return f'<Message: {self.message}>'

# Need to have tables created in order to access this form
db.create_all()
