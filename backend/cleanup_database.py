from app.services.database_cleanup_engine import (
    DatabaseCleanupEngine
)

engine = DatabaseCleanupEngine()

result = engine.run_full_cleanup()

print(result)

engine.close()