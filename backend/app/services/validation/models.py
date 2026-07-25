from dataclasses import dataclass, field
from typing import Any


@dataclass
class ValidationIssue:
    """
    Représente un problème détecté dans une séance.
    """

    level: str          # info | warning | error
    code: str
    message: str


@dataclass
class ValidationReport:
    """
    Résultat complet de la validation d'une séance.
    """

    valid: bool = True

    score: float = 100.0

    issues: list[ValidationIssue] = field(default_factory=list)

    metrics: dict[str, Any] = field(default_factory=dict)

    def add_issue(
        self,
        level: str,
        code: str,
        message: str,
    ) -> None:

        self.issues.append(
            ValidationIssue(
                level=level,
                code=code,
                message=message,
            )
        )

        if level == "error":
            self.valid = False
            self.score -= 25

        elif level == "warning":
            self.score -= 10

        elif level == "info":
            self.score -= 2

        self.score = max(self.score, 0)