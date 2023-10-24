from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    """Aqui irá sua implementação"""
    len_instance = len(instance)
    result = []
    i = 0
    while i < len_instance:
        lines_index_match = []
        file = instance.search(i)
        for line in file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                lines_index_match.append({
                    "linha": file["linhas_do_arquivo"].index(line) + 1,
                    })
        if lines_index_match:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines_index_match,
            })
        i += 1
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    len_instance = len(instance)
    occurrences = exists_word(word, instance)
    for occurrence in occurrences:
        file = occurrence["arquivo"]
        for i in range(len_instance):
            if instance.search(i)["nome_do_arquivo"] == file:
                file = instance.search(i)
                break
        for line in occurrence["ocorrencias"]:
            index = line["linha"] - 1
            line["conteudo"] = file["linhas_do_arquivo"][index]
    return occurrences
