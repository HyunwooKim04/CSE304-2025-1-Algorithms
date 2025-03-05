import unittest
import importlib.util
import sys
import argparse

# 전역 변수로 선언(또는 classmethod 내에서 접근할 수 있도록)
FILE_PATH = None

class TestParkingSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ 주어진 file_path에서 ParkingSystem 클래스를 동적으로 로드해서 리턴 """
        spec = importlib.util.spec_from_file_location("parking_system", FILE_PATH)
        module = importlib.util.module_from_spec(spec)
        sys.modules["parking_system"] = module
        spec.loader.exec_module(module)
        cls.ParkingSystem = module.ParkingSystem

    def test_initialization(self):
        """초기화 테스트"""
        parkingSystem = self.ParkingSystem(2, 3, 1)
        self.assertEqual(parkingSystem.spaces[1], 2)
        self.assertEqual(parkingSystem.spaces[2], 3)
        self.assertEqual(parkingSystem.spaces[3], 1)

    def test_parking_success(self):
        """정상적인 주차 테스트"""
        parkingSystem = self.ParkingSystem(1, 1, 1)
        self.assertTrue(parkingSystem.addCar(1))  # Big car
        self.assertTrue(parkingSystem.addCar(2))  # Medium car
        self.assertTrue(parkingSystem.addCar(3))  # Small car

    def test_parking_failure(self):
        """주차 공간이 없을 때 테스트"""
        parkingSystem = self.ParkingSystem(0, 0, 0)
        self.assertFalse(parkingSystem.addCar(1))  # No big car space
        self.assertFalse(parkingSystem.addCar(2))  # No medium car space
        self.assertFalse(parkingSystem.addCar(3))  # No small car space

    def test_parking_overflow(self):
        """공간보다 많은 차량을 주차할 경우 테스트"""
        parkingSystem = self.ParkingSystem(1, 1, 1)
        self.assertTrue(parkingSystem.addCar(1))  # First big car -> True
        self.assertFalse(parkingSystem.addCar(1)) # Second big car -> False
        self.assertTrue(parkingSystem.addCar(2))  # First medium car -> True
        self.assertFalse(parkingSystem.addCar(2)) # Second medium car -> False
        self.assertTrue(parkingSystem.addCar(3))  # First small car -> True
        self.assertFalse(parkingSystem.addCar(3)) # Second small car -> False

    def test_mixed_parking(self):
        """다양한 크기의 차량 주차 테스트"""
        parkingSystem = self.ParkingSystem(2, 2, 1)
        self.assertTrue(parkingSystem.addCar(1))  # Big car 1 -> True
        self.assertTrue(parkingSystem.addCar(2))  # Medium car 1 -> True
        self.assertTrue(parkingSystem.addCar(3))  # Small car 1 -> True
        self.assertTrue(parkingSystem.addCar(1))  # Big car 2 -> True
        self.assertTrue(parkingSystem.addCar(2))  # Medium car 2 -> True
        self.assertFalse(parkingSystem.addCar(3)) # Small car 2 -> False
        self.assertFalse(parkingSystem.addCar(1)) # Big car 3 -> False
        self.assertFalse(parkingSystem.addCar(2)) # Medium car 3 -> False

    def test_edge_case_zero_slots(self):
        """모든 슬롯이 0개일 때의 엣지 케이스 테스트"""
        parkingSystem = self.ParkingSystem(0, 0, 0)
        self.assertFalse(parkingSystem.addCar(1))
        self.assertFalse(parkingSystem.addCar(2))
        self.assertFalse(parkingSystem.addCar(3))

    def test_large_inputs(self):
        """최대 1000개의 슬롯을 다 채울 수 있는지 테스트"""
        parkingSystem = self.ParkingSystem(1000, 1000, 1000)
        for _ in range(1000):
            self.assertTrue(parkingSystem.addCar(1))
            self.assertTrue(parkingSystem.addCar(2))
            self.assertTrue(parkingSystem.addCar(3))
        self.assertFalse(parkingSystem.addCar(1))
        self.assertFalse(parkingSystem.addCar(2))
        self.assertFalse(parkingSystem.addCar(3))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the student's parking_system.py file")
    args, remaining_args = parser.parse_known_args()
    FILE_PATH = args.file_path
    
    sys.argv = [sys.argv[0]] + remaining_args
    
    unittest.main()
