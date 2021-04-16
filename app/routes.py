from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route("/", methods=['GET', 'POST'])
def home():
    """
    Create a home page for the message board.

    Display a form for users to post messages under their name. Post all messages
    for all visitors to see.

    Parameters
    ----------
    GET
        Method to request data.
    POST
        Method to send data.

    Returns
    -------
    Render the home.html template.
    """
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exists in database
        # Determine who to link the message to
        user = User.query.filter_by(author=form.author.data).first()
        if user is None:
        # if not create user and add to database
            # Allow new users to post messages as well
            user = User(author = form.author.data)
            db.session.add(user)
            db.session.commit()
        # create row in Message table with user (created/found) add to the database
        message = Messages(message = form.message.data, user_id = user.id)
        db.session.add(message)
        db.session.commit()

    posts = []
    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]
    # Follow format for collecting author name and message specified in the home.html template
    list = Messages.query.all()
    for m in list:
        posts.append({'author':User.query.get(m.user_id).author, 'message':m.message})

    return render_template('home.html', posts=posts, form=form)

