import unittest
from main import create_app
from config import TestConfig
from exts import db
from models import Recipe

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        self.client=self.app.test_client(self)

        with self.app.app_context():
            # db.init_app(self.app)

            db.create_all()

    
    def test_HelloWorld(self):
        hello_response = self.client.get('/recipes/hello')
        json_res = hello_response.json
        # print(json_res)
        self.assertEqual(json_res,{"message":"Hello, World!"})

    def test_Signup(self):
        signup_response = self.client.post('/auth/signup',
            json={"username":"testuser",
                      "email":"testuser@test.com",
                      "password":"password"}
        )
        status_code = signup_response.status_code
        self.assertEqual(status_code,201)

    def test_Login(self):
        signup_response = self.client.post('/auth/signup',
            json={"username":"testuser",
                      "email":"testuser@test.com",
                      "password":"password"}
        )
        login_response = self.client.post('/auth/login',
            json={"username":"testuser",
                  "password":"password"}
        )
        status_code = login_response.status_code

        self.assertEqual(status_code,200)

    def test_get_all_recipes(self):
        """TEST GETTING ALL RECIPES"""
        get_recipe_response = self.client.get('/recipes/recipes')
        status_code = get_recipe_response.status_code
        self.assertEqual(status_code,200) 

    def test_get_recipe_by_id(self):
        """TEST GETTING RECIPE BY ID"""
        id = 1
        # with self.app.app_context():
        #     recipe_by_id_response = db.session.get(Recipe,id)
        # if recipe_by_id_response is None:
        #     status_code = 404
        recipe_by_id_response = self.client.get(f'/recipes/recipe/{id}')
        status_code = recipe_by_id_response.status_code
        self.assertEqual(status_code,404)
    
    def test_create_recipe(self):
        signup_response = self.client.post('/auth/signup',
            json={"username":"testuser",
                      "email":"testuser@test.com",
                      "password":"password"}
        )
        login_response = self.client.post('/auth/login',
            json={"username":"testuser",
                  "password":"password"}
        )
        access_token = login_response.json["access token"]

        create_recipe_response = self.client.post('/recipes/recipes',
            json={"title":"Test Recipe",
                  "description":"Test Description"},
            headers = {"Authorization": f"Bearer {access_token}"}
        )
        status_code = create_recipe_response.status_code
        self.assertEqual(status_code,201)
    
    def test_update_recipe(self):
        signup_response = self.client.post('/auth/signup',
            json={"username":"testuser",
                      "email":"testuser@test.com",
                      "password":"password"}
        )
        login_response = self.client.post('/auth/login',
            json={"username":"testuser",
                  "password":"password"}
        )
        access_token = login_response.json["access token"]

        create_recipe_response = self.client.post('/recipes/recipes',
            json={"title":"Test Recipe",
                  "description":"Test Description"},
            headers = {"Authorization": f"Bearer {access_token}"}
        )
        id = 1
        # with self.app.app_context():
        #     get_recipe_by_id_response = db.session.get(Recipe,id)
        # if get_recipe_by_id_response is not None:
        #     status_code = 201

        update_response = self.client.put(f'/recipes/recipe/{id}',
            json={"title":"Test Recipe Updated",
                  "description":"Test Description Updated"},
            headers = {"Authorization": f"Bearer {access_token}"}
        )
        status_code = update_response.status_code
        self.assertEqual(status_code,200)

    def test_delete_recipe(self):
        signup_response = self.client.post('/auth/signup',
            json={"username":"testuser",
                      "email":"testuser@test.com",
                      "password":"password"}
        )
        login_response = self.client.post('/auth/login',
            json={"username":"testuser",
                  "password":"password"}
        )
        access_token = login_response.json["access token"]

        create_recipe_response = self.client.post('/recipes/recipes',
            json={"title":"Test Recipe",
                  "description":"Test Description"},
            headers = {"Authorization": f"Bearer {access_token}"}
        )
        id = 1
        delete_response = self.client.delete(f'/recipes/recipe/{id}',
            headers = {"Authorization": f"Bearer {access_token}"}
            )
        status_code = delete_response.status_code

        self.assertEqual(status_code,200)


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()

