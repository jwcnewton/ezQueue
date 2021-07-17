from src.ezqueue import ezqueue


def test_smoke():
    queue = ezqueue(2)
    expectedQueue = [{"_id": 1, "data": "2"}]
    queue.put(1, "1")
    queue.put(1, "2")

    assert list(queue.getQueue()) == expectedQueue


def test_put_unique_key():
    queue = ezqueue(4)
    expectedQueue = [{"_id": 1, "data": "2"}]
    queue.put(1, "1")
    queue.put(1, "2")

    assert len(queue.getQueue()) != 2
    assert list(queue.getQueue()) == expectedQueue


def test_get_by_id_returns_expected_result():
    queue = ezqueue(2)

    queue.put(1, "1")
    queue.put(2, "2")

    assert queue.getById(2)["data"] == "2"
