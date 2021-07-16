from src.ezqueue.ezqueue import ezqueue


def test_put_unique_key():
    queue = ezqueue(4)

    queue.put(1, "1")
    queue.put(1, "2")

    assert len(queue.getQueue()) != 2
