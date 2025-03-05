import unittest
import importlib.util
import sys
import argparse

# 전역 변수로 선언(또는 classmethod 내에서 접근할 수 있도록)
FILE_PATH = None

class TestRunningSum(unittest.TestCase):
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
        self.assertEqual(solution.runningSum([1,2,3,4]), [1,3,6,10])
        self.assertEqual(solution.runningSum([1,1,1,1,1]), [1,2,3,4,5])
        self.assertEqual(solution.runningSum([3,1,2,10,1]), [3,4,6,16,17])

    def test_single_element(self):
        """배열이 한 개의 원소만 가질 때"""
        solution = self.Solution()
        self.assertEqual(solution.runningSum([5]), [5])

    def test_all_same_numbers(self):
        """모든 원소가 동일한 경우"""
        solution = self.Solution()
        self.assertEqual(solution.runningSum([2,2,2,2,2]), [2,4,6,8,10])

    def test_negative_numbers(self):
        """음수가 포함된 경우"""
        solution = self.Solution()
        self.assertEqual(solution.runningSum([-1,2,-3,4]), [-1,1,-2,2])

    def test_large_numbers(self):
        """큰 수가 포함된 경우"""
        solution = self.Solution()
        self.assertEqual(solution.runningSum([1000000, -1000000, 1000000]), [1000000, 0, 1000000])

    def test_large_input_size(self):
        """길이가 1000인 배열 테스트 (성능 테스트)"""
        solution = self.Solution()
        nums = [1] * 1000
        expected = [i for i in range(1, 1001)]
        self.assertEqual(solution.runningSum(nums), expected)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the student's solution.py file")
    args, remaining_args = parser.parse_known_args()
    FILE_PATH = args.file_path

    sys.argv = [sys.argv[0]] + remaining_args
    
    unittest.main()
