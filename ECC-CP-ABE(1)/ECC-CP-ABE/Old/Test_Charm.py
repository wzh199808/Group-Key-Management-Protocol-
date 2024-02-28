from charm.toolbox.ecgroup import ECGroup,G,ZR
from charm.toolbox.eccurve import prime256v1,prime239v1,prime192v1
from charm.toolbox.eccurve import secp256k1,secp224r1,secp192k1,secp160r1,secp112r1
from charm.toolbox.pairinggroup import PairingGroup,G1,G2,GT,pair
import time
'''
For consistency, group operations are always specified in multiplicative notation, thus ∗ is used for EC point addition and
∗∗ for point multiplication. This makes it easy to switch between group settings.
'''
# Initialize the elliptic curve group of 128-bit security level
group = ECGroup(prime256v1)

g=group.random(G)

p=group.random(G)
q=group.random(G)
print(p)
print(q)
#128-bit security level with bilinear pairing group
pgroup=PairingGroup("BN254")
g1 = pgroup.random(G1)
g2 = pgroup.random(G2)
t1=0
t2=0
t3=0
for i in range(1000):
    ct1=time.perf_counter()
    c = g ** group.random()
    ct2=time.perf_counter()
    c0 = p * q
    ct3=time.perf_counter()
    n = pair(g1, g2)  # BN254pairing 128-bit
    ct4=time.perf_counter()
    t1+=ct2-ct1
    t2+=ct3-ct2
    t3+=ct4-ct3
print(t3,t2,t1)
# group.InitBenchmark()
# # select benchmark options
# group.StartBenchmark([RealTime, Exp, Mul, Add, Sub])
# for a in range(1):
#
# group.EndBenchmark()
# # obtain results
# print(group.GetGeneralBenchmarks())





