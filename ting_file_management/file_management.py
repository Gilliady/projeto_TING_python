import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            extension = file.name.split('.')[1]
            if extension != 'txt':
                print("Formato inválido", file=sys.stderr)
            return file.read().split('\n')
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
