from app.services.load_analyzer import LoadAnalyzer


def test_building_state():

    analyzer = LoadAnalyzer()

    result = analyzer.analyze(
        [100] * 7
    )

    assert result.load_state == "building"


def test_normal_state():

    analyzer = LoadAnalyzer()

    loads = [100] * 28

    result = analyzer.analyze(loads)

    assert result.load_state == "normal"


def test_overload_state():

    analyzer = LoadAnalyzer()

    loads = (
        [300] * 7 +
        [100] * 21
    )

    result = analyzer.analyze(loads)

    assert result.load_state == "overload"