input_case = input()
P,K = input_case.split(' ')
pw = int(P)
key_num = int(K)
def check_password(password, key):
    if key > password :
        return 1000-((key-password)+1)
    elif key == password :
        return 1
    else :
        return password-key+1
print(check_password(pw,key_num))
