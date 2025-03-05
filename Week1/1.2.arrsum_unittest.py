import unittest
import importlib.util
import sys
import argparse

FILE_PATH = None
arrsum = None

def setUpModule():
    global arrsum
    spec = importlib.util.spec_from_file_location("student_module", FILE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["student_module"] = module
    spec.loader.exec_module(module)
    arrsum = module.arrsum

def tearDownModule():
    # 모듈 전체 정리 작업이 필요하면 여기에 추가
    pass

class TestArrSum(unittest.TestCase):
    def test_normal(self):
        # 일반적인 리스트의 합
        self.assertEqual(arrsum(5, [1, 2, 3, 4, 5]), 15)
        self.assertEqual(arrsum(3, [10, 20, 30, 40]), 60)

    def test_empty(self):
        # 빈 리스트 테스트
        self.assertEqual(arrsum(0, []), 0)

    def test_negative(self):
        # 음수 값들이 포함된 리스트 테스트
        self.assertEqual(arrsum(4, [-1, -2, -3, -4]), -10)

    def test_mixed(self):
        # 양수와 음수가 혼합된 경우
        self.assertEqual(arrsum(4, [-1, 2, -3, 4]), 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the student's file containing arrsum")
    args, remaining_args = parser.parse_known_args()
    FILE_PATH = args.file_path

    sys.argv = [sys.argv[0]] + remaining_args
    unittest.main()
