import pytest
from serving.batch_sizing import BatchAdmissionController

def test_empty_queue():
    controller = BatchAdmissionController(max_vram_gb=80.0)
    assert controller.find_max_batch_size(0, lambda x: x * 2.0) == 0

def test_all_requests_fit():
    controller = BatchAdmissionController(max_vram_gb=80.0)
    assert controller.find_max_batch_size(10, lambda x: x * 2.0) == 10

def test_partial_requests_fit():
    controller = BatchAdmissionController(max_vram_gb=80.0)
    assert controller.find_max_batch_size(100, lambda x: x * 3.0) == 26

def test_no_requests_fit():
    controller = BatchAdmissionController(max_vram_gb=20.0)
    assert controller.find_max_batch_size(10, lambda x: x * 25.0) == 0
