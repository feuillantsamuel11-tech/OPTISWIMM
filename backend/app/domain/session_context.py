from dataclasses import dataclass, field


@dataclass
class SessionContext:

    athlete: dict

    specialist: str

    age: int

    race_distance: int

    volume_target: int

    readiness: str

    max_intensity: int

    allow_speed: bool

    used_titles: set = field(default_factory=set)

    primary_objectives: list = field(default_factory=list)

    activation_objectives: list = field(default_factory=list)

    speed_objectives: list = field(default_factory=list)

    week_type: str = "accumulation"

    volume_multiplier: float = 1.0

    intensity_multiplier: float = 1.0

    @property
    def is_deload(self):

        return self.week_type == "deload"

    @property
    def is_shock(self):

        return self.week_type == "shock"