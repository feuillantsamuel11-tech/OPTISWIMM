from app.services.objective_normalizer_engine import (
    ObjectiveNormalizerEngine
)

engine = ObjectiveNormalizerEngine()

result = engine.run()

print("\nNORMALIZATION RESULT:\n")

print(result)

print("\nOBJECTIVES:\n")

for obj in result["objectives"]:

    print(obj)

print("\nCATEGORIES:\n")

for cat in result["categories"]:

    print(cat)

engine.close()