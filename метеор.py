c=1020
ma=1.4*10**21
def boom (m,v):
    Q=(m*v**2)/2
    t=Q/(c*ma)
    if t>50 :
        print("пиздец")
    if t<50 and t>30:
        print("хуевенько")
    elif t<30:
        print("не все потеряно")
boom(10000000000,100000000)