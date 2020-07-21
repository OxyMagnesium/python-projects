import hashlib
import requests

def main():
    pwd_plaintext = input('Enter password to check for: ')
    hasher = hashlib.sha1()
    hasher.update(pwd_plaintext.encode())
    pwd_hashed = hasher.hexdigest()
    
    api_url = 'https://api.pwnedpasswords.com/range/'
    resp = requests.get(api_url + pwd_hashed[ :5])
    hash_list = map(lambda x: x.lower(), resp.text.split('\r\n'))
    
    for hashed in hash_list:
        if pwd_hashed[5: ] in hashed:
            occurances = hashed.split(':')[1]
            print(f'Password occurs in {occurances} breaches!')
            break
    else:
        print('Password not found in any breaches')

if __name__ == '__main__':
    main()
