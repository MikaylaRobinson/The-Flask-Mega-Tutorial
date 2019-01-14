from app import app, db
from app.models import User, Post

'''
Adding this will allow us to test our code in a flask shell without having to import
the database instance and models
'''

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}