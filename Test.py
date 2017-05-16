# coding=utf-8
import random
import ABR
import RB
from timeit import default_timer as timer

# liste di valori random da 1 a 1000, la lunghezza del valore è data da insertion[0]
insertion = [60, 150, 650]
rndvalue = [random.sample(range(1, 1000), insertion[0]), random.sample(range(1, 1000), insertion[1]),
            random.sample(range(1, 1000), insertion[2])]

for i in range(len(insertion)):
    Abr = ABR.ABR()
    AbrRandom = ABR.ABR()
    ARb = RB.RBTree()
    ARbRandom = RB.RBTree()
    for j in range(1, insertion[i]):
        Abr.insert(j)  # inserimento sequenziale
        AbrRandom.insert(rndvalue[i][j])  # inserimento casuale preso dalle liste successive
        ARb.insert(j)
        ARbRandom.insert(rndvalue[i][j])
    print "Caso sequenziale(ABR)\n L' altezza di", insertion[i], "elementi e':", Abr.getRoot().height(Abr.getRoot())
    start = timer()
    Abr.insert(2000)
    end = timer()
    print "Tempo di inserimento di un valore:", end - start, "s"
    print "Caso Random(ABR)\n L'altezza di", insertion[i], "elementi e':", AbrRandom.getRoot().height(AbrRandom.getRoot())
    start = timer()
    AbrRandom.insert(2000)
    end = timer()
    print "Tempo di inserimento di un valore:", end - start, "s"
    print "Caso sequenziale(RB)\n L'altezza di", insertion[i], "elementi e':", ARb.getRoot().height(ARb.getRoot())
    start = timer()
    ARb.insert(2000)
    end = timer()
    print "Tempo di inserimento di un valore:", end - start, "s"
    print "Caso Random(RB)\n L'altezza di", insertion[i], "elementi e':", ARbRandom.getRoot().height(ARbRandom.getRoot())
    start = timer()
    ARbRandom.insert(2000)
    end = timer()
    print "Tempo di inserimento di un valore:", end - start, "s"
    print ""
