# File: check_pacs.py

import os
import subprocess

def check_pacs(pacs_ip_adress, pacs_port, verbose):
    if verbose:
        print("Checking PACS availability")
    try:
        cmd = ['echoscu', pacs_ip_adress, pacs_port]
        if verbose:
            print(" ".join(cmd))
        FNULL = open(os.devnull, 'w') # We don't want the complete output
        p = subprocess.check_output(cmd, timeout=10)
        return True
    # Subprocess timeout
    except subprocess.TimeoutExpired as e:
        if verbose:
            print("\033[31mTimeout: Could not establish connection to PACS: Check adress and port\033[0m")
    except Exception as e:
        if verbose:
            print("\033[31mCould not establish connection\033[0m")
            print(e.stderr)

