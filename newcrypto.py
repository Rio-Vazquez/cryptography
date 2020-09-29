import random
import math
import binascii


# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    answer=""
    for x in plaintext:
        change = ord(x)
        if change + offset > 90:
            change = (change + offset) - 26
        else:
            change = change + offset
        answer = answer + chr(change)
    print(answer)
    return answer

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    result=""
    for x in ciphertext:
        changeback = ord(x)
        if changeback - offset < 65:
            changeback = (changeback - offset) + 26
        else:
            changeback = changeback - offset
        result = result + chr(changeback)
    return result
    

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    rejoinder=""
    y=0
    x=0
    while x<len(plaintext):
        remake = ord(plaintext[x])
        variable = ord(keyword[y])-96
        print(variable)
        if remake + variable > 90:
            remake = (remake + variable) - 26
        else:
            remake = remake + variable
        rejoinder = rejoinder + chr(remake)
        y=y+1
        x=x+1
    return rejoinder

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
        response=""
        x=0
        y=0
        while x<len(ciphertext):
            revamp = ord(ciphertext[x])
            mercurial = ord(keyword[x])-96
            if revamp - mercurial < 65:
                revamp = (revamp - mercurial) + 26
            else:
                revamp = revamp - mercurial
            response = response + chr(revamp)
            x=x+1
            y=y+1
        return response

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    x=0
    total=0
    totalset = []
    while x<n:
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
    # newvar1 = generate_private_key()
    z=0
    while z < 8:
        newset.append(private_key[z])
        z=z+1
    begvar = private_key[8]
    tenthvar = private_key[9]
    finlist = []
    y=0
    while y<8:
        b_i=(begvar*newset[y])%tenthvar
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
        char1 = plaintext[t]
        newval = ord(char1)
        newcharval = get_bin(newval)
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
            cipheranswer.append(c[n])
            n=n+1
        t=t+1
    return cipheranswer

def get_bin(x):
    return format(x, 'b')
    

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    x=0
    solution = ""
    Q = private_key[8]
    R = private_key[9]
    S=random.randint(0, 2*Q)
    while ((R*S)%Q)!=1:
        S=random.randint(0, 2*Q)
    n=0
    newchar = []
    while n < 8:
        newchar.append(int(ciphertext[x*n]))
        n = n + 1
    g = 0
    nextchar = []
    while g < len(ciphertext):
        nextchar.append(ciphertext[g] * S)
        g=g+1
    i = 0
    while i < len(ciphertext):
        if nextchar[i] > private_key[8]:
            nextchar[i] = 1
        else:
            nextchar[i] = 0
        i = i + 1
    t=0
    while x < len(nextchar)/7:
        finalvar = ""
        while t < len(nextchar)/8:
            finalvar = finalvar + str(nextchar[t + (7*x)])
            newfinalvar = int(finalvar) 
            nextascii = 0
            newnext = int(finalvar, 2)
            newlet = chr(newnext)
            if (newlet.isalpha() == True):
                solution = solution + newlet
            t = t + 1
        t=0
        x = x + 1        
    #solution = solution + finalvar
    n=0
    newchar = ""
    return solution

def main():
    

if __name__ == "__main__":
    main()
    
