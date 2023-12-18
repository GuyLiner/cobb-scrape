import sys
import argparse
from municipalities import marietta
from municipalities import cobb

def choose_muni(municipality: str):
    """Chooses what module to run base on the municipality that is entered
    Args:
        municipality (str): Where are you?    
    """
    muni = municipality.lower()

    if muni == "marietta":
        marietta.get_minutes_docs()
    elif muni == "cobb":
        cobb.get_minutes_docs()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-m",
            "--municipality",
            type=str,
            required=True
            )
    args = parser.parse_args()
    choose_muni(args.municipality)