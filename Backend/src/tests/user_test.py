import unittest
from unittest.mock import Mock, patch
from repositories.user import UserRepository
from models.user import User



class TestUserMethods(unittest.TestCase):

    @patch('src.repositories.user.db')
    def test_get_all_users(self, mock_db):
        mock_db.query.return_value.all.return_value = [User()]
        user_repo = UserRepository(mock_db)
        self.assertEqual(len(user_repo.get_all_users()), 1)

#     @patch('src.repositories.user.db')
#     def test_get_user_by_id(self, mock_db):
#         # Configura el mock para devolver un UserRepository
#         mock_db.query.return_value.filter.return_value.first.return_value = UserRepository()
#         user_repo = UserRepository(mock_db)
#         self.assertIsInstance(user_repo.get_user_by_id(1), UserRepository)

#     @patch('src.repositories.user.db')
#     def test_get_user_by_email(self, mock_db):
#         # Configura el mock para devolver un UserRepository
#         mock_db.query.return_value.filter.return_value.first.return_value = UserRepository()
#         user_repo = UserRepository(mock_db)
#         self.assertIsInstance(user_repo.get_user_by_email('test@test.com'), UserRepository)

#     @patch('src.repositories.user.db')
#     def test_delete_user(self, mock_db):
#         # Configura el mock para devolver un UserRepository
#         mock_db.query.return_value.filter.return_value.first.return_value = UserRepository()
#         user_repo = UserRepository(mock_db)
#         self.assertIsInstance(user_repo.delete_user('test@test.com'), UserRepository)

#     @patch('src.repositories.user.db')
#     def test_create_new_user(self, mock_db):
#         # Configura el mock para devolver un UserRepository
#         mock_db.query.return_value.filter.return_value.first.return_value = UserRepository()
#         user_repo = UserRepository(mock_db)
#         # Crea una instancia de User
#         new_user = User(...)
#         self.assertIsInstance(user_repo.create_new_user(new_user), UserRepository)

if __name__ == '__main__':
    unittest.main()