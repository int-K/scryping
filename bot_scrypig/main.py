import os
from flask import Flask, request, abort
import datetime
import calendar
from selenium import webdriver

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello_world"

dt_now = datetime.datetime.now()
dt_now2 = dt_now.isoformat()
wheret = dt_now2.find("T")
wheret2 = dt_now2[wheret:wheret+6]
# print(wheret2)
weekday = datetime.date.today().weekday()
weekday_name = calendar.day_name[weekday]

# print(weekday_name)

# print(weekday)

if weekday_name == "Monday":
    if wheret2 == "T09:30":
        # ローカルに保存しているChrome Driverを指定(※デプロイするときはコメントアウトする)
        # driver_path = "/usr/local/bin/chromedriver"
        # Heroku上のChrome Driverを指定(※デプロイするときはコメントを外す)
        driver_path = '/app/.chromedriver/bin/chromedriver'

        # URL = 'https://www.google.com/?hl=ja'
        URL = "https://pharmatech2020.herokuapp.com/push_test"

        driver = webdriver.Chrome(driver_path)
        driver.get(URL)

        driver.quit()
#         print("Hellow")
    else:
        pass
            
else:
    pass

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)