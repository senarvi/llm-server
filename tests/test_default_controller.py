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
    review = (
        "I recently watched Alex Garland's film Ex Machina, who is also known for films such as Sunshine and "
        "Annihilation. The premise of the film is a young programmer tasked with determining whether an advanced AI "
        "possesses true consciousness, and it explores the interesting philosophical dimensions of artificial "
        "intelligence and consciousness. In general Garland is able to build an interesting atmosphere and the "
        "cinematography is excellent. However, I found that the movie is a bit too slow in the beginning and the "
        "characters are only explored at surface level, which personally left me wanting for a bit more. The issues "
        "the movie tackles are also quite simplified, possibly to make the film a bit more digestible, but I "
        "personally felt that a few less clichés would have improved the film. Reviewed by Jr Robot 123"
    )
    reviewer = "Jr Robot 123"
    body = {"review": review, "reviewer": reviewer}
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
