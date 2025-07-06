#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class in the client module.

Covers:
- Testing org data retrieval via the GitHub API.
- Verifying _public_repos_url property behavior.
- Checking correct handling of repo lists from API responses.
- Validating filtering by license key.
- Integration tests using test fixtures (no real HTTP requests).
"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock
import requests


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test org method returns correct API response"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(
            f'https://api.github.com/orgs/{input}'
        )

    def test_public_repos_url(self):
        """Test _public_repos_url returns expected value"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test public_repos returns correct repo names"""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            expected = [i["name"] for i in json_payload]
            self.assertEqual(result, expected)
            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license correctly filters repos by license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests using fixtures"""

    @classmethod
    def setUpClass(cls):
        """Set up mock requests before all tests in this class"""
        config = {
            'return_value.json.side_effect': [
                cls.org_payload,
                cls.repos_payload,
                cls.org_payload,
                cls.repos_payload
            ]
        }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration test: public_repos method"""
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test with license filtering"""
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(
            test_class.public_repos("apache-2.0"),
            self.apache2_repos
        )
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Tear down mock requests after all tests"""
        cls.get_patcher.stop()
