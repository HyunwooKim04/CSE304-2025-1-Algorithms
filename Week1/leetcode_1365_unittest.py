import unittest
import importlib.util
import sys
import argparse

# 전역 변수로 선언(또는 classmethod 내에서 접근할 수 있도록)
FILE_PATH = None

class TestSmallerNumbers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ 주어진 file_path에서 Solution 클래스를 동적으로 로드해서 리턴 """
        spec = importlib.util.spec_from_file_location("solution", FILE_PATH)
        module = importlib.util.module_from_spec(spec)
        sys.modules["solution"] = module
        spec.loader.exec_module(module)
        cls.Solution = module.Solution

    def test_example_cases(self):
        """기본 제공된 테스트 케이스 검증"""
        solution = self.Solution()
        self.assertEqual(solution.smallerNumbersThanCurrent([8,1,2,2,3]), [4,0,1,1,3])
        self.assertEqual(solution.smallerNumbersThanCurrent([6,5,4,8]), [2,1,0,3])
        self.assertEqual(solution.smallerNumbersThanCurrent([7,7,7,7]), [0,0,0,0])

    def test_sorted_cases(self):
        """정렬된 입력 테스트 (오름차순 & 내림차순)"""
        solution = self.Solution()
        self.assertEqual(solution.smallerNumbersThanCurrent([1,2,3,4]), [0,1,2,3])
        self.assertEqual(solution.smallerNumbersThanCurrent([4,3,2,1]), [3,2,1,0])

    def test_repeated_numbers(self):
        """반복되는 숫자가 포함된 경우"""
        solution = self.Solution()
        self.assertEqual(solution.smallerNumbersThanCurrent([5,5,5,3,1]), [2,2,2,1,0])

    def test_extreme_values(self):
        """제약 조건 경계 값"""
        solution = self.Solution()
        self.assertEqual(solution.smallerNumbersThanCurrent([0, 100, 50]), [0, 2, 1])
        self.assertEqual(solution.smallerNumbersThanCurrent([0, 0, 0]), [0, 0, 0])
        self.assertEqual(solution.smallerNumbersThanCurrent([100, 100, 100]), [0, 0, 0])
        
    def test_mixed_patterns(self):
        """추가 테스트 케이스"""
        solution = self.Solution()
        self.assertEqual(solution.smallerNumbersThanCurrent([1, 3, 5, 3, 1]), [0, 2, 4, 2, 0])
        self.assertEqual(solution.smallerNumbersThanCurrent([10, 10, 5, 8, 5]), [3, 3, 0, 2, 0])
        self.assertEqual(solution.smallerNumbersThanCurrent([11, 3, 7, 9, 3]), [4, 0, 2, 3, 0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the student's solution.py file")
    args, remaining_args = parser.parse_known_args()
    FILE_PATH = args.file_path

    sys.argv = [sys.argv[0]] + remaining_args
    
    unittest.main()
