import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    arquivo1 = {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 1,
        "linhas_do_arquivo": ["linha1"]
    }
    arquivo2 = {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3", "linha4"]
    }
    arquivo3 = {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "linha1",
            "linha2",
            "linha3",
            "linha4",
            "linha5",
            "linha6",
            ]
    }
    arquivo4 = {
        "nome_do_arquivo": "arquivo4.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ["linha1", "linha2"]
    }
    arquivo5 = {
        "nome_do_arquivo": "arquivo5.txt",
        "qtd_linhas": 9,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3", "linha4", "linha5",
                              "linha6", "linha7", "linha8", "linha9"]
    }
    pq = PriorityQueue()
    assert pq.enqueue(arquivo5) is None
    assert len(pq) == 1
    assert pq.search(0) is arquivo5
    pq.enqueue(arquivo4)
    pq.enqueue(arquivo3)
    pq.enqueue(arquivo2)
    pq.enqueue(arquivo1)
    assert pq.search(0) == arquivo4
    response = pq.dequeue()
    assert response == arquivo4
    with pytest.raises(IndexError):
        pq.search(10)
        
