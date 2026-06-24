def rEquity(lLiquido, pLiquido):
    try:
        roe = (lLiquido / pLiquido) * 100
    except ZeroDivisionError:
        input('ERRO! Divisão por zero.\nCertifique-se de que o Patrimônio Líquido não seja zero.')
        return None
    
    return roe

def eBITDA(lOperacional, depreciacao, amortizacao):
    return lOperacional + depreciacao + amortizacao

def mEBITDA(ebitda, rLiquida):
    try:
        margem_EBITDA = (ebitda / rLiquida) * 100
    except ZeroDivisionError:
        input('ERRO! Divisão por zero.\nCertifique-se de que a Receita Líquida não seja zero.')
        return None
    
    return margem_EBITDA

def returnOiC(nOPAT, rLiquida, pOneroso):
    try:
        roic = (nOPAT / rLiquida + pOneroso) * 100
    except ZeroDivisionError:
        input('ERRO! Divisão por zero.\nCertifique-se de que a Receita Líquida ou o Patrimônio Oneroso não sejam zero.')
        return None

    return roic