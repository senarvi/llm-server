import json
from typing import Dict, List

from aiohttp import web
from litgpt import LLM

from llm_server import util
from llm_server.models.http_validation_error import HTTPValidationError
from llm_server.models.movie_review import MovieReview
from llm_server.models.movie_summary import MovieSummary

llm = LLM.load("TinyLlama/TinyLlama-1.1B-Chat-v1.0")


def parse_grade(response) -> int:
    for char in response:
        if char.isdigit() and int(char) >= 0 and int(char) <= 5:
            return int(char)
    return 3


async def movie_summary_movie_summary_post(request: web.Request, body) -> web.Response:
    """Movie Summary

    :param body:
    :type body: dict | bytes
    """
    movie_review = MovieReview.from_dict(body)
    review = movie_review.review
    reviewer = movie_review.reviewer

    grade = llm.generate(
        f"Predict the grade that the reviewer would give to this movie, as an integer between 0 and 5: {review}"
    )
    title = llm.generate(f"Give a short title for this movie review: {review}")
    summary = llm.generate(f"Write a summary of this movie review: {review}")
    movie_summary = MovieSummary.from_dict(
        {
            "title": title,
            "summary": summary,
            "grade": parse_grade(grade),
            "reviewer": reviewer,
        }
    )

    return web.json_response(movie_summary.to_dict())
