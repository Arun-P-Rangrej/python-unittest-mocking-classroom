from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestSalary(TestCase):
    def setUp(self):
        pass

    def test_max_salary_is_greater_than_min_salary_without_mocking(self):
        dbhelper = DbHelper()
        max_salary = dbhelper.get_maximum_salary()
        min_salary = dbhelper.get_minimum_salary()
        self.assertGreater(max_salary, min_salary)

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary_without_mocking(self, MockDbHelper):
        dbhelper = MockDbHelper()     
        dbhelper.get_maximum_salary.return_value = 1  
        max_salary = dbhelper.get_maximum_salary()   
        min_salary = 0       
        self.assertGreater(max_salary, min_salary)
        dbhelper.get_maximum_salary.return_value = 10
        max_salary = dbhelper.get_maximum_salary()
        min_salary = 9
        self.assertGreater(max_salary, min_salary)
