#Questão 4+

from random import random
import sys
import rpyc
import sys
import random
import time

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

n = int(input("Digite um número: "))

array = []
for i in range (n):
    array.append(random.randint(0,100))

print(array)

conn = rpyc.connect(server, 18861)
start = time.time()
print(conn.root.sum(array))
end = time.time()
print("Tempo de execução: {}".format(end - start))
conn.close()