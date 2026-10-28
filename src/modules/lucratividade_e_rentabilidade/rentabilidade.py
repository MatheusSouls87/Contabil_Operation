def rEquity(lLiquido, pLiquido):
    try:
        return (lLiquido / pLiquido) * 100
    except ZeroDivisionError:
        return None

def eBITDA(lOperacional, depreciacao, amortizacao):
    return lOperacional + depreciacao + amortizacao

def mEBITDA(ebitda, rLiquida):
    try:
        return (ebitda / rLiquida) * 100
    except ZeroDivisionError:
        return None

def encurtedROIC(nOPAT, cInvestido):
    try:
        return (nOPAT / cInvestido) * 100
    except ZeroDivisionError:
        return None

def returnOiC(nOPAT, pLiquido, pOneroso):
    try:
        return (nOPAT / (pLiquido + pOneroso)) * 100
    except ZeroDivisionError:
        return None

def calcular_nopat(lucro_operacional, aliquota_imposto):
    return lucro_operacional * (1 - aliquota_imposto / 100)