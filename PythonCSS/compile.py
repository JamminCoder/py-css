from PyCSS.GenerateCSSClasses import *
import os
import argparse
from app import CSSClasses


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfile", dest="out", help="Output file for compiled CSS")
    args = parser.parse_args()
    if not args.out:
        parser.error("[-] No output file specified. Use -o <outfile>")

    outfile = args.out

    if not outfile.split(".")[-1] == "css":
        print("[-] Output file needs to be a CSS file!!")
        exit()

    if os.path.exists(outfile):
        answer = input("[-] File already exist; do you want to overwrite? [y/N]").lower()

        if answer == "y" or "yes":
            print(f"[+] Overwriting {outfile}.")
        else:
            print("Ok, bye.")
            exit()
    return outfile


out_file = get_args()
GenerateCSSClass(CSSClasses, out_file)
