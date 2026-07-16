from app.services.optiswimm_engine import OptiSwimmEngine


def test_generate():

    engine = OptiSwimmEngine()

    profile = {
        "race_distance": 400,
        "recent_loads": [5000] * 28,
    }

    result = engine.generate(profile)

    assert result is not None
    assert result.session is not None
    assert result.decision is not None
    assert result.knowledge_path is not None
    assert result.explanation is not None
    assert result.explanation.summary
    assert len(result.explanation.reasoning) > 0