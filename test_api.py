import unittest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        """Инициализация тестовых переменных"""
        self.github_api_url = "https://api.github.com"
        self.github_user = os.getenv("GITHUB_USER")
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.repo_name = os.getenv("REPO_NAME")

    def test_repo_lifecycle(self):
        """Тестирование полного жизненного цикла репозитория"""
        # Создание репозитория
        url = f"{self.github_api_url}/user/repos"
        headers = {'Authorization': f'token {self.github_token}'}
        data = {'name': self.repo_name, 'private': False}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn(self.repo_name, response.json().get('name'))

        # Проверка на существование репозитория
        url = f"{self.github_api_url}/repos/{self.github_user}/{self.repo_name}"
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.repo_name, response.json().get('name'))

        # Удаление репозитория
        response = requests.delete(url, headers=headers)
        self.assertEqual(response.status_code, 204)

        # Проверка, что репозиторий был удален
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
