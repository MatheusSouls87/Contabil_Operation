def liq_geral(atvCirculante, rLongoPrazo, pCirculante, eLongoPrazo):
    try:
        return (atvCirculante + rLongoPrazo) / (pCirculante + eLongoPrazo)
    except ZeroDivisionError:
        return None

def liq_corrente(aCirculante, pCirculante):
    try:
        return aCirculante / pCirculante
    except ZeroDivisionError:
        return None

def ccLiquido(aCirculante, pCirculante):
    return aCirculante - pCirculante