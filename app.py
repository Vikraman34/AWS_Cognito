from flask import Flask, request
import boto3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    print(request_data)
    username = request_data.get('username')
    password = request_data.get('password')
    print(username, password)
    client = boto3.client('cognito-idp', 'ap-south-1')
    response = client.initiate_auth(
        ClientId='777fktanjr9jc0d7brvp66vego',
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )
    print(response)
    print('AccessToken', response['AuthenticationResult']['AccessToken'])
    print('RefreshToken', response['AuthenticationResult']['RefreshToken'])
    return response

@app.route('/get_user', methods=['POST'])
def get_user():
    request_data = request.get_json()
    access_token = request_data.get('access_token')
    client = boto3.client('cognito-idp', 'ap-south-1')
    response = client.get_user(
        AccessToken=access_token
    )
    email = ''
    for i in response['UserAttributes']:
        if i['Name'] == 'email':
            email = i['Value']
    print(email)
    context = {'email': email}
    return context

@app.route('/change_password', methods=['POST'])
def change_password():
    request_data = request.get_json()
    old_password = request_data.get('old_pass')
    new_password = request_data.get('new_pass')
    access_token = request_data.get('access_token')
    print(old_password, new_password, access_token)
    client = boto3.client('cognito-idp', 'ap-south-1')
    response = client.change_password(
        PreviousPassword=old_password,
        ProposedPassword=new_password,
        AccessToken=access_token
    )
    print(response)
    return response

@app.route('/forgot_password_sendmail', methods=['POST'])
def forgot_password_sendmail():
    request_data = request.get_json()
    username = request_data.get('username')
    client = boto3.client('cognito-idp', 'ap-south-1')
    response = client.forgot_password(
        ClientId='777fktanjr9jc0d7brvp66vego',
        Username=username
    )
    print(response)
    return response

@app.route('/forgot_password_entercode', methods=['POST'])
def forgot_password_entercode():
    request_data = request.get_json()
    username = request_data.get('username')
    code = request_data.get('code')
    new_password = request_data.get('new_password')

    client = boto3.client('cognito-idp', 'ap-south-1')
    response = client.confirm_forgot_password(
        ClientId='777fktanjr9jc0d7brvp66vego',
        Username=username,
        ConfirmationCode=code,
        Password=new_password
    )
    print(response)
    return response

@app.route('/signup1', methods=['POST'])
def signup1():
    request_data = request.get_json()
    username = request_data.get('username')
    new_password = request_data.get('new_password')
    client = boto3.client('cognito-idp', 'ap-south-1')
    response = client.sign_up(
        ClientId='777fktanjr9jc0d7brvp66vego',
        Username=username,
        Password=new_password
    )
    print(response)
    return response

@app.route('/signup2', methods=['POST'])
def signup2():
    request_data = request.get_json()
    username = request_data.get('username')
    code = request_data.get('code')
    client = boto3.client('cognito-idp', 'ap-south-1')
    response = client.confirm_sign_up(
        ClientId='777fktanjr9jc0d7brvp66vego',
        Username=username,
        ConfirmationCode=code
    )
    print(response)
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=105)