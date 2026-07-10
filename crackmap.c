#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <getopt.h>
#include <sodium.h>
#include <glib.h>

char *hash = NULL;
char *wordlist = NULL;

int parser(int argc, char *argv[]) {
    int opt;
    while((opt = getopt(argc, argv, "h:w:"))!=-1) {
        switch(opt) {
            case 'h':
            hash = optarg;
            break;
            case 'w':
            wordlist = optarg;
            break;
        }
    }
    return 0;
}

int files() {
    char finhash[256];
    char finwordlist[256];
    FILE *fin_hash = fopen(hash, "r");
    FILE *fin_wordlist = fopen(wordlist, "r");
    if(fin_hash != NULL) {
        fgets(finhash, sizeof(finhash), fin_hash);
        g_strchomp(finhash);
        printf("[+] cracking %s\n", finhash);
        fclose(fin_hash);
    } else if (fin_hash == NULL) {
        perror("[-] Invalid file");
        return EXIT_FAILURE;
        fclose(fin_hash);
    }
    if(fin_wordlist != NULL) {
        GPtrArray *lines = g_ptr_array_new_with_free_func(g_free);
        if (sodium_init() < 0) {
                    perror("[-] Hashing init failed");
                    return EXIT_FAILURE;
                }
        while(fgets(finwordlist, sizeof(finwordlist), fin_wordlist)) {
            g_strchomp(finwordlist);
            g_ptr_array_add(lines, g_strdup(finwordlist));
            for(guint b = 0; b < lines->len; b++) {
                char *word = g_ptr_array_index(lines, b);
                unsigned char hashed[crypto_hash_sha256_BYTES];
                crypto_hash_sha256(hashed, (unsigned char *)word, strlen(word));
                char string[crypto_hash_sha256_BYTES *2 + 1];
                sodium_bin2hex(string, sizeof(string), hashed, sizeof(hashed));
                for(guint g = 0; g < lines ->len; g++) {
                    if(strcmp(string, finhash)==0) {
                        printf("[+] Password found: %s\n", word);
                        return EXIT_SUCCESS;
                    } else {
                        continue;
                    }
                }
            }
        }
        fclose(fin_wordlist);
    } else if (fin_wordlist == NULL) {
        perror("[-] Invalid wordlist file");
        fclose(fin_wordlist);
        return EXIT_FAILURE;
    }
    return 0;
}

int main(int argc, char *argv[]) {
    if (parser(argc, argv) == 0) {
        files();
    }
}

