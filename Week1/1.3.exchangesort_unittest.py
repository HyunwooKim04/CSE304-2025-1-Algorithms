import unittest
import importlib.util
import sys
import argparse

FILE_PATH = None
exchangesort = None

def setUpModule():
    global exchangesort
    spec = importlib.util.spec_from_file_location("student_module", FILE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["student_module"] = module
    spec.loader.exec_module(module)
    exchangesort = module.exchangesort

class TestExchangeSort(unittest.TestCase):
    def test_normal(self):
        # 일반적인 리스트 정렬 테스트
        S = [4, 2, 5, 1, 3]
        expected = sorted(S)
        exchangesort(len(S), S)
        self.assertEqual(S, expected)

    def test_empty(self):
        # 빈 리스트 테스트
        S = []
        exchangesort(0, S)
        self.assertEqual(S, [])

    def test_already_sorted(self):
        # 이미 정렬된 리스트 테스트
        S = [1, 2, 3, 4, 5]
        exchangesort(len(S), S)
        self.assertEqual(S, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        # 중복 요소가 있는 리스트 테스트
        S = [3, 1, 2, 1]
        expected = sorted(S)
        exchangesort(len(S), S)
        self.assertEqual(S, expected)

    def test_single_element(self):
        # 하나의 원소만 있는 경우 테스트
        S = [42]
        exchangesort(1, S)
        self.assertEqual(S, [42])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the student's file containing exchangesort")
    args, remaining_args = parser.parse_known_args()
    FILE_PATH = args.file_path

    sys.argv = [sys.argv[0]] + remaining_args
    unittest.main()