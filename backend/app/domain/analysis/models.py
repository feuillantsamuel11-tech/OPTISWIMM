from dataclasses import dataclass


@dataclass
class AnalysisResult:
    fatigue: str
    readiness: str
    priority_zone: str
    technical_priority: str
    biomechanical_priority: str
    risk_level: str