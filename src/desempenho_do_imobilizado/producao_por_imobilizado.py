def prod_imobilizado(ctProducao, atvImobilizado):
    try:
        pMob = ctProducao / atvImobilizado
    except ZeroDivisionError:
        input('ERROR! Divisão por zero. Aperte [ENTER] para continuar...')
        return None
    
    return pMob