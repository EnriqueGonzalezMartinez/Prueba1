import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n1", dest="num1", type=int)
parser.add_argument("-n2", dest="num2", type=int)
parser.add_argument("-n3", dest="num3", type=int)
params = parser.parse_args()
prom = (params.num1 + params.num2 + params.num3)/3
print("Promedio: ", prom)
