H1 =input().split()
H2=input().split()
H1A= int(H1[0])
H1S =H1[1]
H2A= int(H2[0])
H2S =H2[1]
if (H1A>=19 and H1S == 'M') or (H2A>=19 and H2S == 'M'):
    print(1)
else:
    print(0)