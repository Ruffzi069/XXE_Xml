from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('Signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('pass')
    conf_pas = request.form.get('conf_pass')

    if password != conf_pas:
        return redirect('/signup')
    print(email, name, password, conf_pas)
    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('Login.html')

@auth.route('/logout')
def logout():
    return "You have to Logout over here!"

@auth.route('/data', methods=['POST'])
def process_data():
    xml_data = request.data.decode('utf-8')
    
    try:
        root = ET.fromstring(xml_data)
        user_id = root.find('ID').text
        details = f"Details for user ID: {user_id}"
    except ET.ParseError:
        details = "Could not parse the XML."

    response = make_response(details)
    return response