from .models import ValidationReport
from .rules import ValidationRules, ObjectiveRules


class SessionValidator:

    def validate(
        self,
        session,
        objective=None,
    ):

        report = ValidationReport()

        # -------------------------
        # Total volume
        # -------------------------

        total = getattr(session, "total_volume", 0)

        if total < ValidationRules.MIN_TOTAL_VOLUME:
            report.add_issue(
                "warning",
                "LOW_VOLUME",
                "Total volume below recommended minimum.",
            )

        if total > ValidationRules.MAX_TOTAL_VOLUME:
            report.add_issue(
                "warning",
                "HIGH_VOLUME",
                "Total volume above recommended maximum.",
            )

        # -------------------------
        # Required blocks
        # -------------------------

        blocks = getattr(session, "blocks", {})

        for block_name in ValidationRules.REQUIRED_BLOCKS:

            if (
                block_name not in blocks
                or not blocks[block_name]
            ):

                report.add_issue(
                    "error",
                    f"MISSING_{block_name.upper()}",
                    f"Missing required block: {block_name}",
                )

        # -------------------------
        # Objective validation
        # -------------------------

        if objective:
            self.validate_objective(
                session,
                objective,
                report,
            )

        return report

    def validate_objective(
        self,
        session,
        objective,
        report,
    ):

        allowed = ObjectiveRules.OBJECTIVE_ZONE.get(objective)

        if not allowed:
            return

        zones = getattr(session, "zones", {})

        if not zones:
            return

        dominant = max(
            zones,
            key=zones.get,
        )

        if dominant not in allowed:

            report.add_issue(
                "warning",
                "OBJECTIVE_MISMATCH",
                (
                    f"Dominant zone ({dominant}) "
                    f"is inconsistent with objective "
                    f"{objective}."
                ),
            )