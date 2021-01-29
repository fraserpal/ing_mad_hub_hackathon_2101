import requests


def post_score(team, metrics):
    ave_reward_list, successful, last_position_episodes = metrics

    EPISODE_THRESHOLD = 10000

    if len(last_position_episodes) < EPISODE_THRESHOLD:
        print(f"Not enough episodes. Minimum required {EPISODE_THRESHOLD}")
        return

    score = last_position_episodes[:EPISODE_THRESHOLD]

    if not isinstance(score, list):
        print("'Score' should be a list of numbers!")
        return
    if not score:
        print("'Score' is empty!")
        return
    if not isinstance(team, str):
        print("'Team' should be a string!")
        return

    try:
        score_avg = sum(score)/len(score)
        success_avg = sum(successful)/len(successful)
        reward_avg = sum(ave_reward_list)/sum(ave_reward_list)
    except Exception:
        score_avg = 0
        success_avg = 0
        reward_avg = 0

    score_url = "https://hackathon-ing-mad-hub-2101.herokuapp.com/score"
    score_query = "?team={}&score={}&successful={}&reward={}"

    r1 = requests.post(score_url + score_query.format(team, [score_avg], [success_avg], [reward_avg]))

    print(r1.text)
