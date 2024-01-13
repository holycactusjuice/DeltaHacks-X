from flask import Blueprint, render_template, request, flash
import pymongo
import bcrypt

auth = Blueprint('auth', __name__)
client = pymongo.MongoClient("mongodb+srv://annikaxu19:b4wE9gtG9KIvQMiG@cluster0.6puxho6.mongodb.net/")
db = client.get_database("total_records")
users = db.users

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error') #flash shows a message on the screen
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'firstname': firstName, 'email':email, 'password':hashed}
            users.insert_one(user_input)

            user_data = users.find_one({"email":email})
            new_email = user_data["email"]

            flash('Account created!', category='success')
            return render_template('signedin.html')

    return render_template('signup.html')

