#wap to find the sum of index positions of digits in a given string.
s=input()
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        sum+=ip
        print(sum)
