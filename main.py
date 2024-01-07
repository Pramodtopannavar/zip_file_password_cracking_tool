import zipfile
from tqdm import tqdm
import itertools

zip_file="123.zip"
zip_file=zipfile.ZipFile(zip_file)

character_set="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
max_password_length=4

n_words=len(character_set)**max_password_length
print("Total paassword to test:",n_words)
for password_length in range(1,max_password_length+1):
    for word in tqdm(itertools.product(character_set,repeat=password_length),total=len(character_set)**password_length,unit="word"):
        password="".join(word)
        try:
            zip_file.extractall(pwd=password.encode())
        except:
            continue
        else:
            print("[+] password found:",password)
            exit(0)
print("[!] Password not found,try longer password or different character set.")
