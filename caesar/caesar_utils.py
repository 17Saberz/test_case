def caesarCipher(s, k):
    res=""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                res+=chr(ord('A')+(ord(s[i])-ord('A')+k)%26)
            else:
                res+=chr(ord('a')+(ord(s[i])-ord('a')+k)%26)    
        else:
            res+=s[i]
    return res

if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)