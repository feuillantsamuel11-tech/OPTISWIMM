class ScoringEngine:

    def score(
        self,
        exercise,
        objective=None,
        zone=None,
    ):

        score = 0

        # objectif
        if objective:
            if objective in getattr(exercise, "objectives", []):
                score += 50

        # zone énergétique
        if zone:
            if getattr(exercise, "zone", None) == zone:
                score += 50

        return score