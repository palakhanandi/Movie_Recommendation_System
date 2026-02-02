import  requests
OMDB_API_KEY = "23ea0969"
r = requests.get(f"https://www.omdbapi.com/?t=Inception&apikey={OMDB_API_KEY}")
print(r.json())