from Crypto.Util.number import isPrime
import gmpy2

gmpy2.get_context().precision=1000
ct = gmpy2.mpz('66888784942083126019153811303159234927089875142104191133776750131159613684832139811204509826271372659492496969532819836891353636503721323922652625216288408158698171649305982910480306402937468863367546112783793370786163668258764837887181566893024918981141432949849964495587061024927468880779183895047695332465')
pubkey = gmpy2.mpz('577080346122592746450960451960811644036616146551114466727848435471345510503600476295033089858879506008659314011731832530327234404538741244932419600335200164601269385608667547863884257092161720382751699219503255979447796158029804610763137212345011761551677964560842758022253563721669200186956359020683979540809')

# Start bruteforce using step system
r = gmpy2.mpz(2**256)
step = r // 2

while True:
    n = 51*r**4 + 88*r**3 + 128680*r**2 + 134636*r + 9816209

    if n > pubkey:
        print('Greater', r)
        # go down a step
        r -= step

    elif n < pubkey:
        print('Less', r)
        # undo the step, then decrease the step size
        r += step
        print('>> Divide step')
        step //= 2

    elif n == pubkey:
        print('Equal', r)
        break

# Calculate primes
p =  3 * r**2 +  2 * r + 7331
q = 17 * r**2 + 18 * r + 1339
print('>> Found r =', r)
print('>> Found p =', p)
print('>> Found q =', q)

# Assert the results
assert (n == (p * q))
assert (isPrime(p) and isPrime(q))
assert ((r%2) == 0 )
assert (r.bit_length() == 256)


# Choose two large distinct primes p and q. One may choose 
# p === q === 3 mod 4 to simplify the computation of 
# square roots modulo p and q 
assert (p % 4 == 3)
assert (q % 4 == 3)

# Decrypt functions
def egcd(a, b):
    # Extended Euclidean algorithm: ax + by == gcd(a, b)
    # This function returns a tuple of (gcd, x, y)
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def decrypt_rabin(c, p, q):
    n = p * q

    # Given p % 4 == 3, q % 4 == 3
    # Equation is: Mp = c^(1/4 * (p+1)) mod p
    Mp = pow(c, (p + 1) // 4, p)
    Mq = pow(c, (q + 1) // 4, q)

    # By applying the extended Euclidean algorithm,
    # we wish to find Yp and Yq such that Yp*p + Yq*q = 1
    gcd, Yp, Yq = egcd(p, q)
    if gcd != 1:
        raise Exception('No modular inverse')

    # By Chinese remainder theorem, the four square roots
    # are calculated
    r = (Yp * p * Mq + Yq * q * Mp) % n
    neg_r = n - r

    s = (Yp * p * Mq - Yq * q * Mp) % n
    neg_s = n - r

    # One of these square roots is the original plaintext m
    return [r, neg_r, s, neg_s]

def hex_pair(x):
    x = '%02x' % x
    return ('0' * (len(x) % 2)) + x

# Decrypt messages, I also swapped p and q because it
# results in different outputs
plaintext = []
plaintext.extend(decrypt_rabin(ct, p, q))
plaintext.extend(decrypt_rabin(ct, q, p))
for m in plaintext:
    print(bytes.fromhex(hex_pair(m)))
    print()
