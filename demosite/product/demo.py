import boto3
import pycognito
# username = 'vikraman.somu@gaincredit.com'
# password = '9443316537_Viki'
#
# client = boto3.client('cognito-idp', 'ap-south-1')
# response = client.initiate_auth(
#     ClientId='777fktanjr9jc0d7brvp66vego',
#     AuthFlow='USER_PASSWORD_AUTH',
#     AuthParameters={
#         'USERNAME': username,
#         'PASSWORD': password
#     }
# )
#
# # print(response)
#
# print('AccessToken', response['AuthenticationResult']['AccessToken'])
# print('RefreshToken', response['AuthenticationResult']['RefreshToken'])

u = pycognito.Cognito('ap-south-1', '777fktanjr9jc0d7brvp66vego', username='vikraman.somu@gaincredit.com')
u.authenticate(password='9443316537_Viki')
print(u)