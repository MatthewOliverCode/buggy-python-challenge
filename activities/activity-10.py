import requests
response = requests.get("https://kennyoliver.github.io/apis/testing/fake-user-data.json")
print(response.status_code)
data = response.json()
print(data)
print(data[0])
print(data[0]["id"])
print(data[0]["first_name"])
print(data[0]["last_name"])
print(data[0]["email"])
print(data[0]["username"])

if data[0]["id"] is data[1]["id"] - 1:
    print(True)
else:
    print(False)

print("-" * 20)

index = 4
if data[index]["email"].startswith(data[index]["first_name"][0].lower() + data[index]["last_name"].title().upper() + str(data[index]["id"])):
    print(True)
else:
    print(False)
