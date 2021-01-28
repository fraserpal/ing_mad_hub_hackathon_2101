import requests


def post_score(team, score):
    score_url = "https://hackathon-ing-mad-hub-2101.herokuapp.com/score"
    score_query = "?team={}&score={}"

    r1 = requests.post(score_url + score_query.format(team, score))

    print(r1.text)


