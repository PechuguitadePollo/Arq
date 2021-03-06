from ta2_c import esPen, hallarHex
import timeit

# Similar al segundo algoritmo, solo que usa funciones
# compiladas con ayuda de Cython
def hallar():
   n = 143
   aux = 0
   while True:
      n = n + 1;
      aux = hallarHex(n)

      if esPen(aux):
         break

def main():
   times = 1000
   t = timeit.timeit('hallar()', setup = "from __main__ import hallar", number = times)
   print "Se demoro " + str((t / times) * 1000) + " ms"

main()
