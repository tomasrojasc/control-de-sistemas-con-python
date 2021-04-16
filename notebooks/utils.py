import control 
import numpy as np

class PID(control.TransferFunction):
    def __init__(self, k_p, k_i, k_d):
        """
        Clase que representa el bloque PID a la que hay que entregar
        k_p, k_i y k_d que son las constantes de proporción proporcional, 
        integral y diferencial respectivamente.
        """
        p = control.TransferFunction([k_p], [1])
        i = control.TransferFunction([k_i], [1, 0])
        d = control.TransferFunction([k_d, 0], [1])
        pid = p + i + d
        
        super().__init__(pid.num[0][0], pid.den[0][0])
        
def closed_loop(tf):
    num = tf.num[0][0]
    den = tf.den[0][0]
    n = num
    d = np.polyadd(num, den)
    return control.TransferFunction(n, d)
