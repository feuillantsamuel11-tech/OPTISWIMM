class ExplanationEngine:

    def build(
        self,
        decision,
        knowledge_path,
        session,
    ):
        explanation = {
            "decision": decision,
            "knowledge_path": knowledge_path,
            "session": session,
        }

        return explanation