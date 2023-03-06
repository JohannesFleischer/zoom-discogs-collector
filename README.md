# discogs-collector
Uses Discogs-API to collect information from your collection on Discogs.

## Installation

```sh
pip install -r packages.txt
```

```sh
python main.py
```

## Usage

Input: <a href="https://www.discogs.com/de/settings/developers">Discogs Token</a>

Output: csv of all your tracks from your whole collection with following data

- Id
- Title
- Artist
- Comment ("Vinyl")
- Duration (millisec)
- Genre
- Track
- Year
- Album
- Label

Need to do: 
- Catalog Nr (Labelcode)
- Date downloaded/created
- Date added
- Style / Subgenre
- Format
- RPM
- Century
