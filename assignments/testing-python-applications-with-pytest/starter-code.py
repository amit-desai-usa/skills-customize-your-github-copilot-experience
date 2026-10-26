def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def highest_score(scores):
    return min(scores)


def passing_scores(scores, pass_mark=60):
    return [score for score in scores if score > pass_mark]