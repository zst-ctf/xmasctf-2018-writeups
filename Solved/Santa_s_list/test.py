#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
import binascii

c = 7455329383143038957429716815165500715158261560971896601396739132805957525166191202455760978408719432329362021224459206704248836452011818476672175430764537075040063368230228365358727043987687964871609661287101362363672847396656546249922690106513698797211955466172034302181014173372680092234399540927971670
n = 8520637787114918832237015248786294009169540917255965331119398471430390846334537463412527582570236972202263403305377799932127000612183588324716119238697948964827609505124731694163461569741661957620860552493085730019676068317580085380871714045570573263756460672395119961317987254629107413356208040537606803
e = 65537

primes = [
    2995933781,
    3834414293,
    # 29016696161674138919369908219,
    2768743379, 3827198227, 2738320643,
    # 9572493988312872677,
    2985009899, 3206855023,
    2165051023,
    # 42605294858361493736155069859,
    4128749161, 3382545863, 3050713213,
    2917169771,
    4105673113,
    2705398837,
    4136392301,
    2700707419,
    3734994139,
    2349776251,
    2625712321,
    4007479051,
    2636514667,
    4048500331,
    4012465003,
    3234818243,
    3639907571,
    2597208121,
    3435673511,
    2674573939,
    2960117663,
    4075003727,
    2758927781,
    2162211553
]

phi = 1
for prime in primes:
    phi *= (prime-1)

e = 65537

# Took from SO
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

# https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
d1 = d = modinv(e, phi)
print("d(e) =", d1)
d2 = d = modinv(e*e, phi)
print("d2(e*e) =", d2)


# ex + py = 1
# ex === 1 (mod phi)

# e*e*w + py = 1
# e*e*w === 1 (mod phi)

d2a = (d1 // e)
print("d2a(e*e) =", d2a)


d5 = modinv(e*e*e*e*e, phi)
print("d5 =", d5)
d5a = (d1 // e // e // e // e // e)
print("d5a(e*e) =", d5a)


# get plaintext
m = pow(c, d1, n)

c = pow(m, e, n)
c2 = pow(c, e, n)
#m = pow(c2, d2, n)


'''
print("c =", c)
print("n =", n)
print("e =", e)
print("d =", d)
print("m =", hex(m))
'''

def hex_pair(x):
    return ('0' * (len(x) % 2)) + x

m_hex = '{:x}'.format(m)
m_hex = hex_pair(m_hex)
msg = binascii.unhexlify(m_hex)
print(msg.decode(errors="ignore"))