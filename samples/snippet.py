def score_move(distance, visible_target, penalty):
    score = 100 - distance * 4
    if visible_target:
        score += 25
    if penalty:
        score -= 40
    return max(score, 0)
