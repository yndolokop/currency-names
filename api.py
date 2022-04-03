from flask import Flask
import requests
import json

# text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
#
# print(text)
#
# currency = json.loads(text)
#
# print(currency['Valute'])

# for currencies in currency['Valute']:
#     print(currencies)

app = Flask(__name__)

@app.route("/")
def hello() -> str:
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currency = json.loads(text)
    result = ''
    for currencies in currency['Valute']:
        result += str(currencies) +'<br>'
    return result

if __name__ == "__main__":
    app.run(debug=False)
