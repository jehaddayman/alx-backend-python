#!/usr/bin/env python3
"""Integration tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from client import GithubOrgClient
import fixtures


@parameterized_class([
    {
        "org_payload": fixtures.ORG_PAYLOAD,
        "repos_payload": fixtures.REPOS_PAYLOAD,
        "expected_repos": fixtures.EXPECTED_REPOS,
        "apache2_repos": fixtures.APACHE2_REPOS
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Patch requests.get and set up mocks"""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        # Define side effects based on request URL
        def side_effect(url):
            if url == "https://api.github.com/orgs/test":
                return Mock(**{"json.return_value": cls.org_payload})
            elif url == cls.org_payload["repos_url"]:
                return Mock(**{"json.return_value": cls.repos_payload})
            return Mock(**{"json.return_value": {}})

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()
