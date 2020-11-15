import argparse
from os import path
from pathlib import Path


class Parser:
    def __init__(self):
        self.args = self.parse_arguments()
        self.output_path = self.is_existing()

    def is_existing(self):
        if path.exists(self.args.output_path):
            return self.args.output_path
        else:
            raise "{} does not exist".format(self.args.output_path)

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-o",
            "--output_path",
            type=Path,
            help="Output path for the generated website with the heatmap.",
            required=True,
        )

        return parser.parse_args()
