import requests
import bs4

# link = "https://icanhazip.com/"
# response = requests.get(link).text
#     print("Success")
# print(response)
link = "https://vk.com/feed"
Status_code = requests.get(link)
response = requests.get(link).text
if Status_code.status_code == 200:
    print("success")
print(response)


