import unittest
import importlib.util
import sys
import argparse

# 전역 변수로 선언 (또는 classmethod 내에서 접근할 수 있도록)
FILE_PATH = None
seqsearch = None 

def setUpModule():
    global seqsearch
    spec = importlib.util.spec_from_file_location("seqsearch_module", FILE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["seqsearch_module"] = module
    spec.loader.exec_module(module)
    seqsearch = module.seqsearch

class TestSeqSearch(unittest.TestCase):
    def test_element_found(self):
        """리스트에서 특정 원소를 찾았을 때의 테스트"""
        self.assertEqual(seqsearch(5, [10, 20, 30, 40, 50], 30), 2)
        self.assertEqual(seqsearch(4, [1, 2, 3, 4], 1), 0)
        self.assertEqual(seqsearch(3, [5, 15, 25], 25), 2)

    def test_element_not_found(self):
        """리스트에 원소가 존재하지 않는 경우 테스트"""
        self.assertEqual(seqsearch(5, [10, 20, 30, 40, 50], 100), -1)
        self.assertEqual(seqsearch(3, [1, 2, 3], 10), -1)

    def test_edge_cases(self):
        """엣지 케이스 테스트"""
        self.assertEqual(seqsearch(0, [], 5), -1)  # 빈 리스트
        self.assertEqual(seqsearch(1, [99], 99), 0)  # 하나만 있을 때 찾기 성공
        self.assertEqual(seqsearch(1, [99], 100), -1)  # 하나만 있을 때 찾기 실패

    def test_duplicates(self):
        """중복 요소가 있는 경우 첫 번째 위치를 반환하는지 테스트"""
        self.assertEqual(seqsearch(6, [1, 2, 3, 2, 5, 2], 2), 1)
        self.assertEqual(seqsearch(6, [7, 7, 7, 7, 7, 7], 7), 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the student's seqsearch.py file")
    args, remaining_args = parser.parse_known_args()
    FILE_PATH = args.file_path
    
    sys.argv = [sys.argv[0]] + remaining_args
    
    unittest.main()
