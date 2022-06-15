# import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format('efjay:blackpandan12345#@localhost:5432', 
                                                         self.database_name)
        setup_db(self.app, self.database_path)


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()


    def tearDown(self):
        """Executed after reach test"""

    """@TODO Write at least one test for each test for successful operation and for expected errors."""


    def test_get_all_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get('success'), True)
        self.assertIn('success', data)
        self.assertIn('categories', data)
        self.assertTrue('total_categories', data)


    def test_no_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(data['total_categories'], 0)
        self.assertNotEqual(len(data['categories']), 0)


    def test_get_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)
        questions = Question.query.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(questions), data['total_questions'])
        self.assertIn('questions', data)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['page'], 1)
        self.assertIn('total_questions', data)
        # self.assertIn('current_category', data)
        self.assertIn('categories', data)


    def test_no_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)
        questions = Question.query.all()

        if len(questions) != 0:
            self.assertNotEqual(len(data['questions']), 0)
            self.assertNotEqual(data['total_questions'], 0)
        else:
            self.assertEqual(len(data['questions']), 0)
            self.assertEqual(data['total_questions'], 0)

            
    def test_delete_question(self):
        response = self.client().delete('/questions/5')
        question = Question.query.get(5)
        data = json.loads(response.data)

        if question is not None:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['deleted_question'], question.id)
            self.assertIn('questions', data)
            self.assertIn('total_questions', data)

   
    def test_delete_question_not_found(self):
        response = self.client().delete('/questions/2000')
        question = Question.query.get(5)
        data = json.loads(response.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 404)
        self.assertIn('message', data)
        self.assertEqual(data['error'], 404)


    def test_wrong_method(self):
        response = self.client().get('/questions/2000')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 405)
        self.assertIn('message', data)
        

    def test_create_question(self):
        response = self.client().post('/questions', json={"question":"Tested",
                                                          "answer":"omo",
                                                          "difficulty":1,
                                                          "category":1
                                                         })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIn("question_created", data)


    def test_cant_create_question(self):
        response = self.client().post('/questions', json={"question":"Tested"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 406)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 406)
        self.assertIn("message", data)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()