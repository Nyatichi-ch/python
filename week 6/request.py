import requests #invita a biblioteca requests
#send message to telegram

response = requests.get('https://api.github.com')
#check if request was successful
if response.status_code == 200:
    print('Request was successful')
else:
    print('Request failed with status code:', response.status_code)
#print the response text
print(response.text)
print(response.headers)
print(response.headers['Content-Type'])
print(response.headers['Content-Length'])
print(response.headers['Server'])
print(response.headers['Date'])
