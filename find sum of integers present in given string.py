#wap to find sum of integers present in given sring.
s=input()
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        sum+=int(s[ip])
        print(sum)
