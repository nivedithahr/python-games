def egcd(a, b):
    s2,s1, t2,t1 = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        s, t = s2-t2*q, s1-t1*q
        b,a, s2,s1, t2,t1 = a,r, t2,t1, s,t
    gcd = b
    return gcd, s2, s1


print(egcd)