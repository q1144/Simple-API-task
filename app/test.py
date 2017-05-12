import unittest
from parser.parser import *
from parser.parse_page import *
from parser.page_queue import *
from app import *

class Test_Get_User_FuntionMethod(unittest.TestCase):
    def test_get_users_result_instanse(self):
        self.assertIsInstance(get_users('https://news.ycombinator.com/news?p=', 1) , tuple)

	def test_get_users_result_is_equal(self):
		self.assertEqual(get_users('https://news.ycombinator.com/news?p=',1) , get_users('https://news.ycombinator.com/news?p=',1)) 

	def test_get_users_result_pages_not_equal(self):
		self.assertNotEqual(get_users('https://news.ycombinator.com/news?p=',1) , get_users('https://news.ycombinator.com/news?p=',2))         
        
    def test_get_users_response_not_empty(self):
		self.assertTrue(len(get_users('https://news.ycombinator.com/news?p=',1)) > 0 )

    def test_get_users_response_not_none(self):
		self.assertIsNotNone(get_users('https://news.ycombinator.com/news?p=',1) )
        

class Test_Parse_Page_FuntionMethod(unittest.TestCase):
    def test_parse_page_result_instanse(self):
        self.assertIsInstance(parse_page('https://news.ycombinator.com/news?p=', 1, 5) , tuple) 

	def test_parse_page_result_is_equal(self):
			self.assertEqual(parse_page('https://news.ycombinator.com/news?p=', 1, 5) , parse_page('https://news.ycombinator.com/news?p=', 1, 5) )

	def test_parse_page_result_pages_not_equal(self):
		self.assertNotEqual(parse_page('https://news.ycombinator.com/news?p=', 1, 5) , parse_page('https://news.ycombinator.com/news?p=', 2, 5) )

	def test_get_users_response_not_empty(self):
			self.assertTrue(len(parse_page('https://news.ycombinator.com/news?p=', 1, 5)) > 0 ) 

	def test_get_users_response_not_none(self):
			self.assertIsNotNone(parse_page('https://news.ycombinator.com/news?p=', 1, 5) ) 		


class Test_Run_Parsing_Queue_Page_FuntionMethod(unittest.TestCase):
    def test_run_parsing_queue_result_instanse(self):
        self.assertIsInstance(run_parsing_queue() , list) 

	def test_get_users_response_not_empty(self):
		self.assertTrue(len(run_parsing_queue()) > 0) 

	def test_get_users_response_not_none(self):
		self.assertIsNotNone(run_parsing_queue() ) 		


class Test_Run_Save_Parsed_Results_FuntionMethod(unittest.TestCase):
	def test_save_parsed_results(self):
		self.assertTrue(save_parsed_results('abc')) 

class Test_Open_Posts_FuntionMethod(unittest.TestCase):
	def test_open_posts_results(self):
		self.assertTrue(open_posts()) 

   
if __name__ == '__main__':
    unittest.main()