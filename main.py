from config import sp

def recommend_songs(genre):

    # Search songs by genre
    results = sp.search(q=f'genre:{genre}', type='track', limit=10)

    tracks = results['tracks']['items']

    print("\nRecommended Songs:\n")

    for i, track in enumerate(tracks, start=1):

        name = track['name']
        artist = track['artists'][0]['name']
        url = track['external_urls']['spotify']

        print(f"{i}. {name} - {artist}")
        print(f"Listen here: {url}\n")


# Ask user for input
genre = input("Enter a music genre: ")

# Call function
recommend_songs(genre)