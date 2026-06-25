import os
from datetime import datetime

extension = ".kpw"
saving_paste = "relatorios"

def existing_paste():
    if not os.path.exists(saving_paste):
        os.makedirs(saving_paste)

def get_full_path(archive_name):
    if not archive_name.endswitch(extension):
        archive_name += extension
    return os.path.join(saving_paste, archive_name)

def create_new_archive(archive_name, description):
    existing_paste()
    pathway =get_full_path(archive_name)

    if os.path.exists(pathway):
        return False
    
    date_curr = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(pathway, "w", encoding="utf-8") as f:
        f.write(f"=== NOME DO PROJETO: {archive_name}{extension} ===\n")
        f.write(f"DESCRIÇÃO: {description}\n")
        f.write(f"CRIADO EM: {date_curr}")
        f.write(f"="*45 + "\n\n")
        f.write("--- HISTÓRICO DE INDICADORES ---\n")
    
    return True

def add_indicator(archive_name, category, indicator, value, nota=""):
    pathway = get_full_path(archive_name)

    if not os.path.exists(pathway):
        return False
    
    date_curr = datetime().now().strftime("%d/%m/%Y %H:%M")

    str_value = f"{value:.2f}" if value is not None else "ERRO/INVÁLIDO"

    with open(pathway, "a", encoding="utf-8") as f:
        f.write(f"[{date_curr}] | Categoria: {category} | Indicador: {indicator} | Valor: {str_value} | Nota: {nota}\n")
    
    return True

def list_files():
    existing_paste()

    archive = [arq for arq in os.listdir(saving_paste) if arq.endswitch(extension)]

    return archive

def read_files(archive_name):
    pathway = get_full_path(archive_name)

    if not os.path.exists(pathway):
        return None

    with open(pathway, "r", encoding="utf-8") as f:
        content = f.read()

    return content