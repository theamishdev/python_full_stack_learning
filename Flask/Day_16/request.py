import requests
response= requests.get("https://jsonplaceholder.typicode.com/posts").json()
print(response)

print(type(response))