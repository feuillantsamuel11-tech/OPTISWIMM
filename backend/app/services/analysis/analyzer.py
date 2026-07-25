from app.domain.analysis.models import AnalysisResult


class AnalysisEngine:

    def analyze(self, context):

        return AnalysisResult(
            fatigue="normal",
            readiness="good",
            priority_zone=context.target_zone,
            technical_priority="none",
            biomechanical_priority="none",
            risk_level="low",
        )