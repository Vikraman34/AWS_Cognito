from django.shortcuts import render, redirect
import boto3

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        if str(request.POST['username']) != '':
            username = str(request.POST['username'])
            password = str(request.POST['pass1'])
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
            request.session['id_token'] = response['AuthenticationResult']['IdToken']
            return redirect(home)
    return render(request, "login.html")

def home(request):
    id_token = request.session.get('id_token')
    print(id_token, "hi")
    return render(request, "home.html")

