# Spotify Music Recommender

A Python-based music recommendation system that integrates with the Spotify API to provide genre-based song recommendations. The application fetches track details such as song names, artists, and Spotify links using API-based search functionality.

---

## Features

* Genre-based music recommendations
* Spotify API integration
* Displays track names and artist information
* Generates direct Spotify links for songs
* Secure API credential management using environment variables

---

## Technologies Used

* Python
* Spotify API
* Spotipy
* Python Dotenv
* Git & GitHub

---

## Project Structure

```bash id="y7wwa5"
spotify-recommender/
│
├── config.py
├── main.py
├── .env
├── .gitignore
└── README.md
```

---

## Installation & Setup

### Clone the Repository

```bash id="j4qz7r"
git clone https://github.com/drishikaaneja/spotify-recommender.git
```

### Navigate to the Project Directory

```bash id="qrcyy2"
cd spotify-recommender
```

### Create a Virtual Environment

```bash id="r4u2mb"
python -m venv .venv
```

### Activate the Virtual Environment

#### macOS/Linux

```bash id="el78k8"
source .venv/bin/activate
```

#### Windows

```bash id="4xbjlwm"
.venv\Scripts\activate
```

---

## Install Dependencies

```bash id="yfgjji"
pip install spotipy python-dotenv
```

---

## Spotify API Configuration

Create a `.env` file in the root directory and add the following credentials:

```env id="5s6l1d"
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```

Spotify Developer Dashboard:
https://developer.spotify.com/dashboard

---

## Running the Application

```bash id="5b7p8z"
python main.py
```

Enter a music genre when prompted to receive song recommendations.

---

## Future Enhancements

* Web-based interface using Streamlit
* Mood and artist-based recommendations
* Playlist generation
* Machine Learning-based personalized recommendations

---

## Author

Drishika Aneja
