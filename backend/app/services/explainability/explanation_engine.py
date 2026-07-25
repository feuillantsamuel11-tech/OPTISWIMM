from app.services.explainability.models import Explanation


class ExplanationEngine:

    def build(
        self,
        decision,
        knowledge_path=None,
        session=None,
    ):

        reasoning = []

        # Raisonnement du DecisionEngine
        if decision and getattr(decision, "reasoning", None):
            reasoning.extend(decision.reasoning)

        # Résumé
        if decision and getattr(decision, "objectives", None):
            objective = decision.objectives[0]
            summary = (
                f"Session générée pour l'objectif '{objective}'."
            )
        else:
            summary = "Session générée."

        # Confiance
        confidence = (
            getattr(decision, "confidence", 0.0)
            if decision
            else 0.0
        )

        # Détails
        details = {}

        if decision:

            details["specialist"] = getattr(
                decision,
                "specialist",
                None,
            )

            details["load_state"] = getattr(
                decision,
                "load_state",
                None,
            )

            details["objectives"] = getattr(
                decision,
                "objectives",
                [],
            )

        if knowledge_path:

            details["knowledge_path"] = knowledge_path

        if session:

            details["session"] = session

        return Explanation(
            summary=summary,
            reasoning=reasoning,
            confidence=confidence,
            details=details,
        )