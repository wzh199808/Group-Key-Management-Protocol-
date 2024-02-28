from charm.toolbox.ecgroup import ECGroup,ZR,G
from charm.toolbox.eccurve import prime192v1

trials = 10
group = ECGroup(prime192v1)
g = group.random(G)
h = group.random(G)
i = group.random(G)

assert group.InitBenchmark(), "failed to initialize benchmark"
group.StartBenchmark(["Mul", "Div", "Exp", "Granular"])
for a in range(trials):
    j = g * h
    k = h ** group.random(ZR)
    t = (j ** group.random(ZR)) / k

group.EndBenchmark()

msmtDict = group.GetGeneralBenchmarks()
print("<=== General Benchmarks ===>")
print("Mul := ", msmtDict["Mul"])
print("Div := ", msmtDict["Div"])
print("Exp := ", msmtDict["Exp"])
granDict = group.GetGranularBenchmarks()
print("<=== Granular Benchmarks ===>")
print("G mul   := ", granDict["Mul"][G])
print("G exp   := ", granDict["Exp"][G])