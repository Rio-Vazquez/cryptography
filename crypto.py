import random
import math
import binascii


# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    answer=""
    for x in plaintext:
        if (ord(x) <123) and (64<ord(x)):
            change = ord(x)
            if change + offset > 90:
                change = (change + offset) - 26
            else:
                change = change + offset
            answer = answer + chr(change)
        else:
            answer = answer + x
    return answer

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    result=""
    for x in ciphertext:
        if (ord(x) <123) and (64<ord(x)):
            changeback = ord(x)
            if changeback - offset < 65:
                changeback = (changeback - offset) + 26
            else:
                changeback = changeback - offset
            result = result + chr(changeback)
        else:
            result = result + x
    return result
    
# Makes sure the key can be strecthed to fit the string
# Arguments: string, string
# Returns: string
def make_vigenere_key(new, key):
    newdata = key
    NOGI = len(newdata)
    if len(newdata) == len(new):
        return newdata
    else:
        x = NOGI
        while x < len(new):
            newdata = newdata + newdata[x-NOGI]
            x = x + 1
    return newdata


# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    secretinfo = make_vigenere_key(plaintext, keyword)
    rejoinder=""
    x=0
    while x<len(plaintext):
        remake = ord(plaintext[x])
        variable = ord(secretinfo[x]) - 97
        if remake < 91:
            variable = ord(secretinfo[x]) - 65
            if remake + variable > 90:
                remake = (remake + variable) - 26
            else:
                remake = remake + variable
        elif remake + variable > 122:
            remake = (remake + variable) - 26
        else:
            remake = remake + variable
        rejoinder = rejoinder + chr(remake)
        x=x+1
    return rejoinder

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
        secretinfo2 = make_vigenere_key(ciphertext, keyword)
        response=""
        x=0
        while x<len(ciphertext):
            revamp = ord(ciphertext[x])
            mercurial = ord(secretinfo2[x])-97
            if revamp < 91:
                mercurial = ord(secretinfo2[x]) - 65
                if revamp - mercurial < 65:
                    revamp = (revamp - mercurial) + 26
                else:
                    revamp = revamp - mercurial
            elif revamp - mercurial < 97:
                revamp = (revamp - mercurial) + 26
            else:
                revamp = revamp - mercurial
            response = response + chr(revamp)
            x=x+1
        return response

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    x=0
    total=0
    totalset = []
    while x < 8:
       newvar=random.randint(total+1, 2*(total+1))
       total=total+newvar
       totalset.append(newvar)
       x=x+1
    nextvar=random.randint(total+1, 2*total)
    finvar=random.randint(2, nextvar)
    while math.gcd(finvar, nextvar)!=1:
        finvar=random.randint(2, nextvar)
    nexttotalset =  []
    g = 0
    while g < 8:
        nexttotalset.append(totalset[g])
        g=g+1
    nexttotalset.append(nextvar)
    nexttotalset.append(finvar)
    return nexttotalset


# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    newset = []
    z=0
    while z < 8:
        newset.append(private_key[z])
        z=z+1
    Q = private_key[8]
    R = private_key[9]
    finlist = []
    y=0
    while y<8:
        b_i=(R*newset[y])%Q
        finlist.append(b_i)
        y=y+1
    B = tuple(finlist)
    return B


# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    z = len(plaintext)
    t=0
    cipheranswer = []
    while t<z:
        text1 = 0
        char1 = plaintext[t]
        newval = ord(char1)
        newcharval = '{0:08b}'.format(newval)
        w = 0
        m = []
        # newpublickey = array(public_key)
        while w < len(newcharval):
            m.append(int(newcharval[w]))
            w = w + 1
        c = []
        b = 0
        while b < len(m):
            c.append(public_key[b] * m[b])
            b = b + 1
        n=0
        while n < len(c):
            text1 = text1 + c[n]
            n=n+1
        cipheranswer.append(text1)
        t=t+1
    return cipheranswer

def get_bin(x):
    return format(x, 'b')

    
def greed_is_good(cprime1, private_key):
    Y = []
    variable = cprime1
    while variable > 0:
        top = 0
        answer = 0
        x=0
        while x < 8:
            if private_key[x] > top and private_key[x] <= variable:
                top = private_key[x]
                answer = x
            x = x + 1
        answer1 = int(answer)
        Y.append(answer1)
        variable = variable - top
    return Y



# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    x=0
    solution = ""
    Q = private_key[8]
    R = private_key[9]
    S=random.randint(0, 2*Q)
    while (R*S%Q)!=1:
        S=random.randint(0, 2*Q)
    newchar = []
    cprime = []
    y=0
    while y < len(ciphertext):
        cprime.append((ciphertext[y] * S)%Q)
        y = y + 1
    n = 0
    while n < len(cprime):
        cprime2 = greed_is_good(cprime[n], private_key)
        total = 0
        g = 0
        while g < len(cprime2):
            exponent1 = cprime2[g]
            total = total + 2**(8-exponent1)
            g = g + 1
        char122 = chr(int(total/2))
        solution = solution + char122
        n = n + 1   
    print(solution)     
    #solution = solution + finalvar
    n=0
    newchar = ""
    return solution

def main():
    pass

if __name__ == "__main__":
    main()
    
