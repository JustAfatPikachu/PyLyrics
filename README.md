# Lyrics Typewriter

A Python script that fetches song lyrics from Genius and displays them in a typewriter-style effect, skipping all bracketed sections like `[Verse]`, `[Chorus]`, `[Bridge]`, etc. The lyrics are also saved as a JSON file for reuse.

---

## Features

- Fetch lyrics from Genius API using song and artist names  
- Skip bracketed sections automatically (`[Verse]`, `[Chorus]`, `[Bridge]`)  
- Typewriter effect with customizable speed  
- Save lyrics as JSON in the same folder  

---

## Requirements

- Python 3.8+  
- Packages:
  - `lyricsgenius`  

> Note: `time` and `json` are built-in Python modules, so no installation required.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/JustAFatPikachu/PyLyrics.git
cd <repo-name>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Get your own Genius API token:
   - Go to [Genius API](https://genius.com/developers)  
   - Sign up or log in  
   - Create a new API client  
   - Copy the access token  

---

## Usage

Run the file:

python lyrics_typewriter.py

You will be prompted to enter:

1. Your Genius API token  
2. The song name  
3. The artist name  

The script will:

- Fetch the song lyrics from Genius  
- Save them as a JSON file (`<song_name>.json`)  
- Display the lyrics with a typewriter effect, skipping bracketed sections

### Example Input

```text
Enter your Genius API token: <YOUR_TOKEN>
Enter the song name: Blinding Lights
Enter the artist name: The Weeknd
```

### Example Output

```
I've been tryna call
I've been on my own for long enough
Maybe you can show me how to love, maybe
I'm going through withdrawals
You don't even have to do too


> Bracketed sections like `[Verse 1]`, `[Chorus]`, `[Bridge]` are skipped automatically.

---

## Typewriter Speed

Adjust the speed by editing the `time.sleep()` value in the script:

```python
time.sleep(0.09)  # shorter = faster, longer = slower
```

Optionally, make newlines slightly longer for a more natural feel:

```python
if char == "\n":
    print()
    time.sleep(0.3)  # longer pause for line breaks
```

---

## Notes

- Only works for songs with lyrics available on Genius.  
- Each user should use their **own Genius API token** to avoid hitting rate limits.  
- JSON files are saved in the same directory as the script.  
- Bracketed annotations are skipped automatically.

---

## License

This project is for personal and educational use. Please do not abuse Genius API tokens.
