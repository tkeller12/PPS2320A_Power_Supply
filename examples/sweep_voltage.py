import numpy as np
import pps
import time


ps = pps.pps()

print(ps)


voltages = np.r_[0:1:100j]


ps.output(True)
for v_ix, v in enumerate(voltages):

    print(v_ix,v)
    try:
        ps.voltage(v)
    except:
        print('Communication Failed!')
        try:
            ps.voltage(v)
        except:
            print('Communication Failed Twice!')
            pass

    time.sleep(0.1)


ps.output(False)
del ps
