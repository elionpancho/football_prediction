import requests

url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

querystring = {"market":"classic","iso_date":"2018-12-01","federation":"UEFA"}

headers = {
	"x-rapidapi-key": "54840ff97cmsh32c90f471cf78d2p1779b1jsnd96faae30ef7",
	"x-rapidapi-host": "football-prediction-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())