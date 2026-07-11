from app.services.session_engine.fatigue_manager import FatigueManager


class MetricsCalculator:

    def __init__(self):

        self.fatigue = FatigueManager()

    def calculate(self, exercises):

        total_volume = self.fatigue.calculate_volume(
            exercises
        )

        total_cns = self.fatigue.calculate_cns_load(
            exercises
        )

        average_intensity = (
            self.fatigue.calculate_average_intensity(
                exercises
            )
        )

        fatigue_state = (
            self.fatigue.get_fatigue_state(
                total_cns
            )
        )

        return {

            "total_volume": total_volume,

            "total_cns": total_cns,

            "average_intensity": average_intensity,

            "fatigue_state": fatigue_state,
        }