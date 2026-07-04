from dataclasses import dataclass


@dataclass(slots=True)
class LoadAnalysis:

    acute_load: float
    chronic_load: float
    acwr: float
    load_state: str


class LoadAnalyzer:

    def analyze(self, recent_loads):

        acute_load = sum(recent_loads[:7])

        if len(recent_loads) < 28:

            return LoadAnalysis(
                acute_load=acute_load,
                chronic_load=0,
                acwr=1.0,
                load_state="building",
            )

        chronic_load = sum(recent_loads[:28]) / 4

        acwr = (
            acute_load / chronic_load
            if chronic_load > 0
            else 1.0
        )

        if acwr > 1.5:
            state = "overload"

        elif acwr < 0.8:
            state = "underload"

        else:
            state = "normal"

        return LoadAnalysis(
            acute_load=acute_load,
            chronic_load=chronic_load,
            acwr=acwr,
            load_state=state,
        )