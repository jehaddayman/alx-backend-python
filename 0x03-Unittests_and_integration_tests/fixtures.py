ORG_PAYLOAD = {
    "login": "test",
    "repos_url": "https://api.github.com/orgs/test/repos"
}

REPOS_PAYLOAD = [
    {"name": "repo1", "license": {"key": "apache-2.0"}},
    {"name": "repo2", "license": {"key": "other"}}
]

EXPECTED_REPOS = ["repo1", "repo2"]
APACHE2_REPOS = ["repo1"]
