import json

import pytest
from aiohttp import web

from llm_server.models.http_validation_error import HTTPValidationError
from llm_server.models.movie_review import MovieReview
from llm_server.models.movie_summary import MovieSummary

pytestmark = pytest.mark.asyncio


async def test_movie_summary_movie_summary_post(client):
    """Test case for movie_summary_movie_summary_post

    Movie Summary
    """
    body = {"review": "review", "reviewer": "reviewer"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = await client.request(
        method="POST",
        path="/movie_summary",
        headers=headers,
        json=body,
    )
    assert response.status == 200, "Response body is : " + (await response.read()).decode("utf-8")
