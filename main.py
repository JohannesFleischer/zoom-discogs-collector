#! python3

import track as t
import discogs_client as dc
from discogs_client.exceptions import HTTPError
from retry import retry
from time import sleep
import csv
import os


def main():
    # user input
    token = input("Paste your token: \n")
    filename = input("Please enter the name of the csv file: \n") + ".csv"

    # connect to discogs client with token
    client = dc.Client("DiscogsCollector", user_token=token)

    # creates list of all releases of the personal user collection
    release_ids = [
        release.id for release in client.identity().collection_folders[0].releases
    ]

    # delete file if exists (otherwise multiple executions would append the data to the same file)
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

        foo(release_ids, client, writer)


@retry(HTTPError, delay=5, tries=-1)
def foo(release_ids, client, writer):
    # releases
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

            logging(id, year, album, artist, label, genre, star_track, duration)

            writer.writerow(t.Track.get_values(track))

            # TODO sleep -> proxys
            # sleep for bigger collections (mayhaps a little less than 0.5 sec)
            sleep(0.5)


def logging(id, year, album, artist, label, genre, star_track, duration):
    print("id: " + str(id))
    print("year: " + year)
    print("album: " + album)
    print("artist: " + artist)
    print("label: " + label)
    print("genre: " + genre)
    print("title: " + star_track.title)
    print("position: " + star_track.position)
    print("duration: " + str(duration))
    print("------------------------------")


if __name__ == "__main__":
    main()
