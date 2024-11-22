#wap to check how many times the given substring is present in given string.
s=input()
sub=input()
c=0
for ip in range(len(s)):
    if s[ip:ip+len(sub):]==sub:
        c+=1
        print(s[ip:ip+len(sub):])
print(c)
  
