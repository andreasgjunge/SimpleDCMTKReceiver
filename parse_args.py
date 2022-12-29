# File: parse_args.py

import argparse

def parse_args():
    # Set up the argument parser
    parser = argparse.ArgumentParser()

    # Add the "-c" and "--config" arguments
    parser.add_argument("-c", "--config", action="store_true", help="Read and print out the configuration and exit")

    # Add the "-c" and "--config" arguments
    parser.add_argument("-p", "--pacs-check", action="store_true", help="Check PACS availability and exit")

    # Add the "-f" argument
    parser.add_argument("-f", "--file-name", dest="csv_file_name", type=str, help="Specify the filename of the CSV file containing the study instance uids")

    # Add the "-d" and "--dry-run" arguments
    parser.add_argument("-d", "--dry-run", action="store_true", help="Create and print out the movescu commands, but do not initiate move")

    # Add the "-v" and "--verbose" arguments
    parser.add_argument("-v", "--verbose", action="store_true", help="Print out additional information")

    # Parse the command line arguments
    return parser.parse_args()
