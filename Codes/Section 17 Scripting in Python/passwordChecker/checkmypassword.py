import requests
import hashlib
import sys

#url = 'https://api.pwnedpasswords.com/range/' + 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'
#res = requests.get(url)
#print(res)

# K anoynmity means show only first 5. The api will return top all hashed
# passwords with first 5 letters as stated

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times.. Please change your password')
        else:
            print(f'{password} was not found. Please continue')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
#request_api_data('CBFDA')
# Never store password in generic text
# hashing can be done here

# Hash generates a unique value for every oinput it gets. It is one way
# GiVEN INPUT, WE CAN GET OUTPUT (BUT NOT OTHER WAY AROUND)
# Key features of hash functions
# 1. Its one way (given hash no one can know what the input is)
# 2. No matter how many time i input my actual text, output is same
# 3. Small change in input (even one letter), the Hash changes a lot
# 4. Idempotent: function given an input always output same output

# https://passwordsgenerator.net/sha1-hash-generator/
