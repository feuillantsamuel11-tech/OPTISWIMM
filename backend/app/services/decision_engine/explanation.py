class ExplanationEngine:

    def explain(self, decision):

        return "\n".join(decision.reasoning)