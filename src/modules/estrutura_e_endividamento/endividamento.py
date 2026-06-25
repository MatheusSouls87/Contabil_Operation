def relacaoCTCP(cTerceiros, cProprio):
    try:
        rCTCP = (cTerceiros / cProprio) * 100
    except ZeroDivisionError:
        input('ERRO! Divisão por zero.\nCertifique-se de que Capital Próprio - Passivo Total - não seja zero.')
        return None
    
    return rCTCP

def comp_ENDIVIDAMENTO(pCirculante, pNCirculante):
    try:
        cEndividamento = (pCirculante / (pCirculante + pNCirculante)) * 100
    except:
        input('ERRO! Divisão por zero.\nCertifique-se de que o Passivo Circulante ou o Passivo Não Circulante não sejam zero.')
        return None
    
    return cEndividamento