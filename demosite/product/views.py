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
            request.session['access_token'] = response['AuthenticationResult']['AccessToken']
            return redirect(home)
    return render(request, "login.html")

def home(request):
    access_token = request.session.get('access_token')
    client = boto3.client('cognito-idp', 'ap-south-1')
    response = client.get_user(
        AccessToken=access_token
    )
    email=''
    for i in response['UserAttributes']:
        if i['Name'] == 'email':
            email = i['Value']
    print(email)
    context = {'email': email}
    return render(request, "home.html", context)


def change_password(request):
    if request.method == 'POST':
        if str(request.POST['pass1']) != '':
            old_password = str(request.POST['pass1'])
            new_password = str(request.POST['pass2'])
            access_token = request.session.get('access_token')
            print(old_password, new_password, access_token)
            client = boto3.client('cognito-idp', 'ap-south-1')
            response = client.change_password(
                PreviousPassword=old_password,
                ProposedPassword=new_password,
                AccessToken=access_token
            )
            print(response)
            return redirect(index)
    return render(request, "change_password.html")

def forgot_password1(request):
    if request.method == 'POST':
        if str(request.POST['username']) != '':
            username = str(request.POST['username'])
            print(username)
            client = boto3.client('cognito-idp', 'ap-south-1')
            response = client.forgot_password(
                ClientId='777fktanjr9jc0d7brvp66vego',
                Username=username
            )
            print(response)
            return redirect(forgot_password2)
    return render(request, "forgot_password1.html")

def forgot_password2(request):
    if request.method == 'POST':
        if str(request.POST['username']) != '':
            username = str(request.POST['username'])
            code = str(request.POST['code'])
            new_password = str(request.POST['pass1'])
            print(username, code, new_password)
            client = boto3.client('cognito-idp', 'ap-south-1')
            response = client.confirm_forgot_password(
                ClientId='777fktanjr9jc0d7brvp66vego',
                Username=username,
                ConfirmationCode=code,
                Password=new_password
            )
            print(response)
            return redirect(index)
    return render(request, "forgot_password2.html")

def sign_up1(request):
    if request.method == 'POST':
        if str(request.POST['username']) != '':
            username = str(request.POST['username'])
            new_password = str(request.POST['pass1'])
            print(username, new_password)
            client = boto3.client('cognito-idp', 'ap-south-1')
            response = client.sign_up(
                ClientId='777fktanjr9jc0d7brvp66vego',
                Username=username,
                Password=new_password
            )
            print(response)
            return redirect(sign_up2)
    return render(request, "sign_up1.html")

def sign_up2(request):
    if request.method == 'POST':
        if str(request.POST['username']) != '':
            username = str(request.POST['username'])
            code = str(request.POST['code'])
            print(username, code)
            client = boto3.client('cognito-idp', 'ap-south-1')
            response = client.confirm_sign_up(
                ClientId='777fktanjr9jc0d7brvp66vego',
                Username=username,
                ConfirmationCode=code
            )
            print(response)
            return redirect(index)
    return render(request, "sign_up2.html")