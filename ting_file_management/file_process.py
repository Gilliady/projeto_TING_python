import sys
from queue import Queue
from .file_management import txt_importer


def process(path_file: str, instance: Queue):
    """Aqui irá sua implementação"""
    lines = txt_importer(path_file)
    try:
        output = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
          }
        instance.enqueue(output)
        print(output, file=sys.stdout)
    except ValueError:
        print("Arquivo já adicionado", file=sys.stderr)


def remove(instance: Queue):
    """Aqui irá sua implementação"""
    try:
        file = instance.dequeue()
        print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso",
              file=sys.stdout)
    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        print(instance.search(position), file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
