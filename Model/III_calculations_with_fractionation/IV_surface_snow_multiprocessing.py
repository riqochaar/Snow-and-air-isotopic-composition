# This file was used to call 'IV_surface_snow_calculation.py'

# Multiprocessing was employed to save on computing time

import pandas as pd
import joblib
import numpy as np
import multiprocessing
from IV_surface_snow_calculation import isotope

S = range(0,1441,60)


if __name__ == "__main__":

     a = multiprocessing.Process(target=isotope, args=(S[0], S[1], '01', 0.001))
     b = multiprocessing.Process(target=isotope, args=(S[1], S[2], '02', 0.001))
     c = multiprocessing.Process(target=isotope, args=(S[2], S[3], '03', 0.001))
     d = multiprocessing.Process(target=isotope, args=(S[3], S[4], '04', 0.001))
     e = multiprocessing.Process(target=isotope, args=(S[4], S[5], '05', 0.001))
     f = multiprocessing.Process(target=isotope, args=(S[5], S[6], '06', 0.001))

     g = multiprocessing.Process(target=isotope, args=(S[6], S[7], '07', 0.001))
     h = multiprocessing.Process(target=isotope, args=(S[7], S[8], '08', 0.001))
     i = multiprocessing.Process(target=isotope, args=(S[8], S[9], '09',  0.001))
     j = multiprocessing.Process(target=isotope, args=(S[9], S[10], '10', 0.001))
     k = multiprocessing.Process(target=isotope, args=(S[10], S[11], '11', 0.001))
     l = multiprocessing.Process(target=isotope, args=(S[11], S[12], '12', 0.001))

     m = multiprocessing.Process(target=isotope, args=(S[12], S[13], '13', 0.001))
     n = multiprocessing.Process(target=isotope, args=(S[13], S[14], '14', 0.001))
     o = multiprocessing.Process(target=isotope, args=(S[14], S[15], '15', 0.001))
     p = multiprocessing.Process(target=isotope, args=(S[15], S[16], '16', 0.001))
     q = multiprocessing.Process(target=isotope, args=(S[16], S[17], '17', 0.001))
     r = multiprocessing.Process(target=isotope, args=(S[17], S[18], '18', 0.001))

     s = multiprocessing.Process(target=isotope, args=(S[18], S[19], '19', 0.001))
     t = multiprocessing.Process(target=isotope, args=(S[19], S[20], '20', 0.001))
     u = multiprocessing.Process(target=isotope, args=(S[20], S[21], '21', 0.001))
     v = multiprocessing.Process(target=isotope, args=(S[21], S[22], '22', 0.001))
     w = multiprocessing.Process(target=isotope, args=(S[22], S[23], '23', 0.001))
     x = multiprocessing.Process(target=isotope, args=(S[23], S[24], '24', 0.001))

     a.start()
     b.start()
     c.start()
     d.start()
     e.start()
     f.start()

     g.start()
     h.start() 
     i.start()
     j.start()
     l.start()
     k.start()

     m.start()
     n.start()
     o.start()
     p.start()
     q.start()
     r.start()

     s.start()
     t.start()
     u.start()
     v.start()
     w.start()
     x.start()

     a.join()
     b.join()
     c.join()
     d.join()
     e.join()
     f.join()

     h.join()
     g.join()
     i.join()
     j.join()
     k.join()
     l.join()

     m.join()
     n.join()
     o.join()
     p.join()
     q.join()
     r.join()

     s.join()
     t.join()
     u.join()
     v.join()
     w.join()
     x.join()


