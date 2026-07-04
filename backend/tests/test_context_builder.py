from app.services.context_builder import AthleteContextBuilder


def test_context_builder():

    builder = AthleteContextBuilder()

    athlete, context = builder.build(

        athlete_profile={

            "specialist": "middle_distance",

            "race_distance": 200,

        }

    )

    assert athlete["race_distance"] == 200

    assert context.race_distance == 200

    assert context.specialist == athlete["specialist"]