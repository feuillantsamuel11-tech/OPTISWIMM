from app.services.validation import ValidationReport


def test_validation_report_defaults():

    report = ValidationReport()

    assert report.valid is True
    assert report.score == 100
    assert report.issues == []


def test_add_warning():

    report = ValidationReport()

    report.add_issue(
        "warning",
        "HIGH_VOLUME",
        "Volume élevé",
    )

    assert len(report.issues) == 1
    assert report.score == 90
    assert report.valid is True


def test_add_error():

    report = ValidationReport()

    report.add_issue(
        "error",
        "NO_MAIN_SET",
        "Main set absent",
    )

    assert report.valid is False
    assert report.score == 75