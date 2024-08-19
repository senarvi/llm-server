#!/usr/bin/env python

from litgpt import LLM

llm = LLM.load("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

review = (
    "I recently watched Alex Garland's film Ex Machina, who is also known for films such as Sunshine and Annihilation. The premise of the film is a young "
    "programmer tasked with determining whether an advanced AI possesses true consciousness, and it explores the interesting philosophical dimensions of artificial "
    "intelligence and consciousness. In general Garland is able to build an interesting atmosphere and the cinematography is excellent. However, I found that the movie is a "
    "bit too slow in the beginning and the characters are only explored at surface level, which personally left me wanting for a bit more. The issues the movie tackles are "
    "also quite simplified, possibly to make the film a bit more digestible, but I personally felt that a few less clichés would have improved the film. Reviewed by Jr Robot "
    "123"
)

summary = llm.generate(f"Summarize the movie review: {review}")

print(summary)
