# CrackMap
# Description:
Crackmap is a pot file free hashcracker that can be reused, it cracks hashes for the algorithms sha256, sha512, md5, and sha1, (for the python version) (the C version only cracks sha256 for now) give it a txt file with the hash in it and a txt file with the wordlist and it will crack the hash
# Usage:
python3 hashmap.py -m {your mode} -p {your_hash_file.txt} -w {your_wordlist_file.txt} (for the python version)
gcc crackmap.c -o crackmap -lsodium `pkg-config --cflags --libs glib-2.0`
./crackmap -h {your your_hash_file.txt} -w {your_wordlist_file.txt} (for the C version)
# Disclaimer:
please only use in permitted enviornments
