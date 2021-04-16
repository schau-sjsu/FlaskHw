from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    """
    Represent the form for a message board.

    Attributes
    ----------
    author : StringField
        Name of the author of the message
    message : StringField
        Message to be posted to the board
    submit : SubmitField
        Button to post the message to the message board
    """
    # add
    # author (string) validator should make this textbox required
    author = StringField('author', validators=[DataRequired()])
    # message (string) validator should make this textbox required
    message = StringField('message', validators=[DataRequired()])
    # submit (button) text should say 'Send'
    submit = SubmitField('Send')
