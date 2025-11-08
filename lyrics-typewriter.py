from lyricsgenius import Genius
import json
import time
token = input("Enter your Genius Api token: ")
song_name = input("Enter the song name: ")
artist_name = input("Enter the artist name: ")
genius = Genius(token)
song = genius.search_song(song_name, artist_name)

if song:
    with open(f"{song_name}.json", "w", encoding="utf-8") as f:
        json.dump(song.to_dict(), f, ensure_ascii=False, indent=2)

with open(f"{song_name}.json", "r")as file:
    data = json.load(file)

def load():
    in_brackets = False
    for char in data["lyrics"]:
        if char == "]":
            in_brackets = False
            continue
        elif in_brackets:
            continue
        elif char =="[":
            in_brackets = True
            continue
        else:
            print(char, end="", flush =True)
            time.sleep(0.09)


    print()

load()