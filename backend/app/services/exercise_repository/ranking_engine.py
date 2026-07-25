class RankingEngine:

    def rank(self, exercises):

        return sorted(
            exercises,
            key=lambda e: getattr(e, "score", 0),
            reverse=True,
        )