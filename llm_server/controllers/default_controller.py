from typing import Dict, List

from aiohttp import web

from llm_server import util
from llm_server.models.http_validation_error import HTTPValidationError
from llm_server.models.movie_review import MovieReview
from llm_server.models.movie_summary import MovieSummary


async def movie_summary_movie_summary_post(request: web.Request, body) -> web.Response:
    """Movie Summary



    :param body:
    :type body: dict | bytes

    """
    body = MovieReview.from_dict(body)
    return web.Response(status=200)
