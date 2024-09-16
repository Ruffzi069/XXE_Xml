from flask import (Blueprint, make_response, redirect, render_template,
                   request, url_for)
from lxml import etree as ET

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
    # Decode the incoming XML data
    xml_data = request.data.decode('utf-8')
    parser = ET.XMLParser(resolve_entities=True)
    root = ET.fromstring(xml_data, parser=parser)
    try:
        # Parse XML data with lxml, allowing external entity resolution
        # Enable external entity resolution
        # parser = ET.XMLParser(resolve_entities=True)
        #  Parse the XML with XXE vulnerability enabled
        # root = ET.fromstring(xml_data, parser=parser)

        # Extract the user ID from the XML
        user_id = root.find('ID').text
        print(user_id)
        details = open(
            f'static/details/{user_id.replace('\n', '')}').read()
    except ET.XMLSyntaxError:
        # If parsing fails, return the raw XML (this simulates error handling)
        details = __import__('os').getcwd()
    except:
        details = f"Current working directory: {__import__('os').getcwd()}"

    response = make_response(details)
    return response
