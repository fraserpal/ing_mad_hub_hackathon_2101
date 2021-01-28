import requests


def post_score(team, score):
    if not isinstance(score, list):
        print("'Score' should be a list of numbers!")
        return
    if not score:
        print("'Score' is empty!")
        return
    if not isinstance(team, str):
        print("'Team' should be a string!")
        return

    score_avg = sum(score)/len(score)

    score_url = "https://hackathon-ing-mad-hub-2101.herokuapp.com/score"
    score_query = "?team={}&score={}"

    r1 = requests.post(score_url + score_query.format(team, [score_avg]))

    print(r1.text)
