#!/usr/bin/env python3
"""Unittests for GithubOrgClient"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ({"license": {"key": "apache-2.0"}}, "apache-2.0", True),
        ({"license": {"key": "mit"}}, "apache-2.0", False),
        ({}, "apache-2.0", False),
        ({"license": None}, "apache-2.0", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license correctly checks the license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
