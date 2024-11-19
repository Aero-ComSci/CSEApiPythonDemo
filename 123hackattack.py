import requests

print("Welcome to the Hack Attack!")

userName = "MiguelBa"
url = "https://cs-api.pltw.org/"
makeuser = "newuser/"
postMessage = "?text="
incrementValue1 = "/increment?id="
call = url+userName
response = requests.get(url+userName)
print(response.text)
if(response.text == "Error: No such user."):
    response = requests.post(url+makeuser+userName)
    print(response.text)

#call = url+userName+postMessage+"Hello%20World!"
call = url+userName+incrementValue1+"1"
#print(call)
#response = requests.post(call)
print(response.text)