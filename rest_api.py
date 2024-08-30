import requests

def bestInGenre(genre):
    base_url = "https://jsonmock.hackerrank.com/api/tvseries"
    page = 1
    best_show = None
    highest_rating = -1
    
    while True:
        # Construct the URL with pagination
        response = requests.get(f"{base_url}?page={page}")
        data = response.json()
        
        # Check if the response contains data
        if 'data' not in data or len(data['data']) == 0:
            break
        
        for show in data['data']:
            if genre.lower() in show['genre'].lower():
                if show['imdb_rating'] > highest_rating:
                    highest_rating = show['imdb_rating']
                    best_show = show['name']
                elif show['imdb_rating'] == highest_rating:
                    if show['name'] < best_show:
                        best_show = show['name']
        
        # Check if there are more pages
        if page >= data['total_pages']:
            break
        page += 1   
    print(best_show)

if __name__ == "__main__":
    bestInGenre("comedy")