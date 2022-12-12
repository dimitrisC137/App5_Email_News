import requests
from send_email import send_email

topic = "tesla"

api_key = "4f84f0c95e97448dba279d5c818d2c67"
url = f"https://newsapi.org/v2/everything?q={topic}&from=" \
      "2022-12-12&sortBy=publishedAt&apiKey=4f84f0c95e97448dba279d5c818d2c67"

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Today;s news"\
            "\n" + body + article["title"] + "\n"  \
            + article["description"] \
            + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
