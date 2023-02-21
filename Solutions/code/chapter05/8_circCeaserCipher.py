def main():
    word = input("Enter word to encrypt: ")
    key = int(input("Enter encryption key: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
    total = ""

    for ch in word:
        cryCh = ord(ch) - 97 + key - 26
        cryChAlph = alphabet[cryCh]
        total = total + cryChAlph
    print(total)
main()