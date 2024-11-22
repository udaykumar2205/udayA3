#wap to find the sum of even index positions of even numbers.
s=input()
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        sum+=ip
        if ip%2==0:
            print(ip,s[ip])
