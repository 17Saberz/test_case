def is_funny_string(s):
    a=s[::-1]
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1]))!=abs(ord(a[i])-ord(a[i+1])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = is_funny_string(s)
        print(result + '\n')