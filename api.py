import requests

url = "https://argentina-movie-theatres.p.rapidapi.com/cinemas"

headers = {
	"X-RapidAPI-Key": "4c24c7d3b7msha9c2def7540d066p12db18jsnc7c423d08cee",
	"X-RapidAPI-Host": "argentina-movie-theatres.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()
for i in range(6, 11):
    print(response[i]['name'])