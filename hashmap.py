#!/usr/bin/env python3

import sys
import hashlib
import argparse
import time

print(r"""
======================================================================================
  ______ .______          ___       ______  __  ___ .___  ___.      ___      .______   
 /      ||   _  \        /   \     /      ||  |/  / |   \/   |     /   \     |   _  \  
|  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  \  /  |    /  ^  \    |  |_)  | 
|  |     |      /      /  /_\  \  |  |     |    <   |  |\/|  |   /  /_\  \   |   ___/  
|  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  |  |  |  /  _____  \  |  |      
 \______|| _| `._____/__/     \__\ \______||__|\__\ |__|  |__| /__/     \__\ | _|       
======================================================================================
""")

print("[+] Welcome to hashmap")
time.sleep(1)

args = argparse.ArgumentParser(add_help=False)
args.add_argument("-p", required=False)
args.add_argument("-m", required=False)
args.add_argument("-w", required=False, type=str)
args.add_argument("-h", required=False, action="store_true")
ex_args = args.parse_args()
hash1 = ex_args.p
mode = ex_args.m
wordlist = ex_args.w
help1 = ex_args.h

def cracking():
    with open (wordlist, "r") as f:
        words = [word.strip() for word in f.readlines()]
    with open (hash1, "r") as f1:
        pass1 = f1.read().strip()
    def hashcrack():
        for word in words:
            try:
                global hashed_word
                if mode == "sha256":
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                elif mode == "sha512":
                    hashed_word = hashlib.sha512(word.encode()).hexdigest()
                elif mode == "md5":
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif mode == "sha1":
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                if hashed_word == pass1:
                    print(f"[+] Password found: {word}")
            except ValueError:
                print("[-] invalid hash")
                sys.exit()
            except KeyboardInterrupt:
                sys.exit()
    hashcrack()
valid_modes= {"sha256", "sha512", "md5", "sha1"}
if mode in valid_modes:
    cracking()
if help1:
    print("""
    
    ==============================================================================
    -m to specify mode, so far this tool supports sha256, sha512, md5, sha1 hashes
    ==============================================================================
    -p to specify the file with the hash in it
    ==============================================================================
    - w to specify wordlist
    ==============================================================================
    
    """)