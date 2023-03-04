import track as t

import discogs_client as dc
import csv
import os

def main():
    token = input("Paste your token: \n")
    client = dc.Client("DiscogsCollector", user_token=token)

    # creates list of all releases of the personal user collection
    release_ids = [
        release.id for release in client.identity().collection_folders[0].releases
    ]

    filename = "tracks.csv"

    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, "a", encoding="UTF8") as file:
        writer = csv.writer(file, delimiter=";")
        header = [
            "id",
            "year",
            "album",
            "artist",
            "label",
            "genre",
            "title",
            "position",  # TODO if empty -> no write
            "duration",
        ]
        writer.writerow(header)

        # albums
        for id in release_ids:
            release = client.release(id)

            year = str(release.year)
            album = release.title
            artist = release.artists[0].name
            label = release.labels[0].name
            genre = release.genres[0]

            tracklist = release.tracklist

            # tracks
            for star_track in tracklist:
                duration = t.Track.duration_to_ms(
                    star_track, duration_raw=star_track.duration
                )
                track = t.Track(
                    id,
                    year,
                    album,
                    artist,
                    label,
                    genre,
                    star_track.title,
                    star_track.position,
                    duration,
                )
                writer.writerow(t.Track.get_values(track))


if __name__ == "__main__":
    main()
