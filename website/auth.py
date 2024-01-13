from flask import Blueprint, render_template, request, flash
<<<<<<< Updated upstream

auth = Blueprint('auth', __name__)
=======
import pymongo
import bcrypt
import certifi

auth = Blueprint('auth', __name__)
client = pymongo.MongoClient("mongodb+srv://yiyanhh:kcyDdQBUnW9Ak6DB@cluster0.hdoctva.mongodb.net/", tlsCAFile=certifi.where())
db = client.get_database("users")
user = db.appname
>>>>>>> Stashed changes

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
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        existing_user = user.find_one({'username': 'happyman'})
        existing_email = user.find_one({'email': email})

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error') #flash shows a message on the screen
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        elif existing_user and username == existing_user['username']:
            flash('That username already exists. Please choose another one')
        elif existing_email and email == existing_email['email']:
            flash('That email is already registered. Please enter another one.')
        else:
<<<<<<< Updated upstream
=======
            user_input = {'firstname': firstName, 'username' : username, 'email':email, 'password': password1}
            user.insert_one(user_input)

            user_data = user.find_one({"email":email})
            new_email = user_data["email"]

>>>>>>> Stashed changes
            flash('Account created!', category='success')

    return render_template('signup.html')

