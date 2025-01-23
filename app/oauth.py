from fastapi_users.providers.oauth2.github import GitHubOAuth2
from fastapi_users.authentication import OAuth2AuthorizeHandler
import os

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

github_oauth = GitHubOAuth2(
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET,
    authorize_handler=OAuth2AuthorizeHandler(redirect_url="http://localhost:8000/auth/github/callback"),
)
