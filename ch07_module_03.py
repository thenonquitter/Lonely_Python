from urllib import request

# target = "https://2selves.com"
response = request.urlopen("https://2selves.com")
output = response.read()
print(output)