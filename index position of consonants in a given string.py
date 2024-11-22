#wap to print index positions of consonants in a given string.
s=input()
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip].isalpha() and s[ip] not in v:
        print(ip,s[ip])
