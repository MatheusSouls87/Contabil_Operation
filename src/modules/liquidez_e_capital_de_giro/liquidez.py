def liq_geral(atvCirculante, rLongoPrazo, pCirculante, eLongoPrazo):
    try:
        liq_Geral = (atvCirculante + rLongoPrazo) / (pCirculante + eLongoPrazo)
    except ZeroDivisionError:
        input('ERRO! Divisão por zero.\nCertifique-se de que o Passivo Circulante e o Exigível a Longo Prazo não sejam zero.')
        return None

    return liq_Geral

def liq_corrente(aCirculante, pCirculante):
    try:
        liq_Corrente = aCirculante / pCirculante
    except ZeroDivisionError:
        input('ERRO! Divisão por zero.\nCertifique-se de que o Passivo Circulante não seja zero.')
        return None
    
    return liq_Corrente

def ccLiquido(aCirculante, pCirculante):
    return aCirculante - pCirculante