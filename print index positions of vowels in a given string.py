#wap to print index positions of vowels in a given string.
s=input()
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip] in v:
        print(ip,s[ip])
    
