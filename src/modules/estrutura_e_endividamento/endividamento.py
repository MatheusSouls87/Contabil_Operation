def relacaoCTCP(cTerceiros, cProprio):
    try:
        return (cTerceiros / cProprio) * 100
    except ZeroDivisionError:
        return None

def comp_ENDIVIDAMENTO(pCirculante, pNCirculante):
    try:
        return (pCirculante / (pCirculante + pNCirculante)) * 100
    except ZeroDivisionError:
        return None