
class DuplicationManager:

    def __init__(self):

        pass

    # =================================================
    # RECENT TITLES
    # =================================================

    def get_recent_titles(

        self,

        recent_sessions
    ):

        titles = []

        for session in recent_sessions:

            blocks = session.get(
                "session",
                {}
            )

            for block_name, exercises in blocks.items():

                for ex in exercises:

                    if isinstance(ex, dict):

                        title = ex.get(
                            "title"
                        )

                        if title:

                            titles.append(
                                title
                            )

        return titles

    # =================================================
    # RECENT OBJECTIVES
    # =================================================

    def get_recent_objectives(

        self,

        recent_sessions
    ):

        objectives = []

        for session in recent_sessions:

            blocks = session.get(
                "session",
                {}
            )

            for block_name, exercises in blocks.items():

                for ex in exercises:

                    if isinstance(ex, dict):

                        objective = ex.get(
                            "objective"
                        )

                        if objective:

                            objectives.append(
                                objective
                            )

        return objectives

    # =================================================
    # TITLE DUPLICATION
    # =================================================

    def is_duplicate_title(

        self,

        title,

        recent_titles
    ):

        return title in recent_titles

    # =================================================
    # OBJECTIVE SATURATION
    # =================================================

    def objective_frequency(

        self,

        objective,

        recent_objectives
    ):

        return recent_objectives.count(
            objective
        )

    # =================================================
    # OBJECTIVE SATURATION STATE
    # =================================================

    def get_saturation_state(

        self,

        frequency
    ):

        if frequency >= 6:

            return "very_high"

        if frequency >= 4:

            return "high"

        if frequency >= 2:

            return "moderate"

        return "low"

    # =================================================
    # SHOULD AVOID OBJECTIVE
    # =================================================

    def should_avoid_objective(

        self,

        objective,

        recent_objectives
    ):

        frequency = (

            self.objective_frequency(

                objective,

                recent_objectives
            )
        )

        return frequency >= 5

    # =================================================
    # FILTER EXERCISES
    # =================================================

    def filter_exercises(

        self,

        exercises,

        recent_titles
    ):

        filtered = []

        for ex in exercises:

            title = getattr(
                ex,
                "title",
                None
            )

            if not self.is_duplicate_title(

                title,

                recent_titles
            ):

                filtered.append(ex)

        return filtered

    # =================================================
    # SESSION VARIETY SCORE
    # =================================================

    def calculate_variety_score(

        self,

        recent_objectives
    ):

        unique = len(
            set(recent_objectives)
        )

        total = len(
            recent_objectives
        )

        if total == 0:

            return 10

        score = (

            unique / total
        ) * 10

        return round(
            score,
            2
        )

    # =================================================
    # BUILD DUPLICATION PROFILE
    # =================================================

    def build_profile(

        self,

        recent_sessions
    ):

        recent_titles = (

            self.get_recent_titles(
                recent_sessions
            )
        )

        recent_objectives = (

            self.get_recent_objectives(
                recent_sessions
            )
        )

        variety_score = (

            self.calculate_variety_score(
                recent_objectives
            )
        )

        saturation = {}

        for objective in set(
            recent_objectives
        ):

            frequency = (

                self.objective_frequency(

                    objective,

                    recent_objectives
                )
            )

            saturation[
                objective
            ] = {

                "frequency":
                frequency,

                "state":
                self.get_saturation_state(
                    frequency
                )
            }

        return {

            "recent_titles":
            recent_titles,

            "recent_objectives":
            recent_objectives,

            "variety_score":
            variety_score,

            "objective_saturation":
            saturation
        }

