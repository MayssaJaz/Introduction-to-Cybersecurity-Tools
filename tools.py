
def verify_primary_numbers(e, phi):
    while(phi != 0):
        e, phi = phi, e % phi
    return e


def prime_check(a):
    if(a == 2):
        return True
    elif((a < 2) or ((a % 2) == 0)):
        return False
    elif(a > 2):
        for i in range(2, a):
            if not(a % i):
                return False
    return True


def pgcd(e, phi):
    for i in range(1, phi):
        while(e != 0):
            a, b = phi//e, phi % e
            if(b != 0):
                print("%d = %d*(%d) + %d" % (phi, a, e, b))
            phi = e
            e = b


def eea(a, b):
    if(a % b == 0):
        return(b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return(gcd, t, s)


def calculate_d(e, phi):
    gcd, s, _ = eea(e, phi)
    if(gcd != 1):
        return None
    else:
        if(s < 0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d." %
                  (s, s, s % phi))
        elif(s > 0):
            print("s=%d." % (s))
        return s % phi
