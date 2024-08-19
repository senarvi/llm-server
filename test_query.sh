#!/bin/bash -e

review="I recently watched Alex Garland's film Ex Machina, who is also known for films such as Sunshine and "
review+="Annihilation. The premise of the film is a young programmer tasked with determining whether an advanced AI "
review+="possesses true consciousness, and it explores the interesting philosophical dimensions of artificial "
review+="intelligence and consciousness. In general Garland is able to build an interesting atmosphere and the "
review+="cinematography is excellent. However, I found that the movie is a bit too slow in the beginning and the "
review+="characters are only explored at surface level, which personally left me wanting for a bit more. The issues "
review+="the movie tackles are also quite simplified, possibly to make the film a bit more digestible, but I "
review+="personally felt that a few less clichés would have improved the film. Reviewed by Jr Robot 123"

reviewer='Jr Robot 123'

set -x
curl -v\
  -X POST\
  -H 'Content-Type: application/json'\
  -d "{\"review\":\"${review}\",\"reviewer\":\"${reviewer}\"}"\
  'http://localhost:8080/movie_summary'
