import argparse
import os
import re
from mutagen.easyid3 import EasyID3
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(description="TERMINAL MP3 METADATA EDITOR")
    parser.add_argument(
        "-f",
        "--folder_path",
        type=Path,
        help="Absolute path to folder containing .mp3 files",
        required=True,
    )

    auxiliary_parser = parser.add_argument_group()
    auxiliary_parser.add_argument("-a", "--artist", help="Artist name", required=False)
    auxiliary_parser.add_argument("-al", "--album", help="Album name", required=False)
    auxiliary_parser.add_argument(
        "-tn", "--tracknumber", help="Track number", type=int, required=False
    )
    auxiliary_parser.add_argument("-t", "--title", help="Track title", required=False)
    auxiliary_parser.add_argument("-g", "--genre", help="Track genre", required=False)

    return parser.parse_args()


def mp3_metadata_editor():

    args = parse_arguments()

    files = sorted(os.listdir(args.folder_path))

    i = args.tracknumber
    title = args.title
    album = args.album
    genre = args.genre
    artist = args.artist

    for audio_path in files:
        audio = EasyID3(os.path.join(args.folder_path, audio_path))
        try:
            audio["title"] = str(title) + " " + str(i)
            audio["artist"] = str(artist)
            audio["album"] = str(album)
            audio["tracknumber"] = str(i)
            audio["genre"] = str(genre)
            audio.save()
            i += 1
        except KeyError:
            raise KeyError("Wrong track key!")
        except ValueError:
            raise ValueError("Invalid data!")


if __name__ == "__main__":
    mp3_metadata_editor()

    print("Formatting successful!")
