from app.services.session_engine.objective_selector import (
    ObjectiveSelector
)

from app.services.session_engine.specialist_manager import (
    SpecialistManager
)
  

from app.services.session_engine.fatigue_manager import (
    FatigueManager
)

from app.services.session_engine.block_builder import (
    BlockBuilder
)


class IntelligentSessionBuilder:

    def __init__(self):

        self.objective_selector = (
    ObjectiveSelector()
)

        self.specialist_manager = (
    SpecialistManager()
)

        self.fatigue_manager = (
    FatigueManager()
)

        self.block_builder = (
    BlockBuilder()
)

    # =================================================
    # CURRENT VOLUME
    # =================================================

    def calculate_current_volume(

        self,

        blocks
    ):

        total = 0

        for block in blocks:

            for ex in block:

                total += ex.get(
                    "volume",
                    0
                )

        return total

    # =================================================
    # REMAINING VOLUME
    # =================================================

    def calculate_remaining_volume(

        self,

        volume_target,

        blocks
    ):

        current = (

            self.calculate_current_volume(
                blocks
            )
        )

        remaining = (
            volume_target
            - current
        )

        return max(
            200,
            remaining
        )

    # =================================================
    # READINESS MODIFIERS
    # =================================================

    def apply_readiness_modifiers(

        self,

        readiness_level,

        volume_target
    ):

        if readiness_level == "high":

            return {

                "volume_target":
                int(volume_target),

                "max_intensity":
                10,

                "allow_speed":
                True
            }

        if readiness_level == "low":

            return {

                "volume_target":
                int(volume_target * 0.60),

                "max_intensity":
                6,

                "allow_speed":
                False
            }

        return {

            "volume_target":
            int(volume_target * 0.80),

            "max_intensity":
            8,

            "allow_speed":
            False
        }
    # =================================================
    # BUILD SESSION
    # =================================================

    def build_session(

        self,

        athlete,

        readiness
    ):

        specialist_profile = (

            self.specialist_manager
            .build_profile(
                athlete
            )
        )

        

        specialist = (
            specialist_profile[
                "specialist"
            ]
        )

        age = specialist_profile[
            "age"
        ]

        volume_target = (
            specialist_profile[
                "volume_target"
            ]
        )

        readiness_level = (
            athlete.get(
                "readiness_state",
                "moderate"
            )
        )

        readiness_profile = (

         self.apply_readiness_modifiers(

         readiness_level,

         volume_target
         )
       )

        volume_target = (

         readiness_profile[
         "volume_target"
        ]
       )

        max_intensity = (

         readiness_profile[
         "max_intensity"
       ]
      )

        allow_speed = (

        readiness_profile[
        "allow_speed"
       ]
    )

        print(
            "READINESS:",
            readiness_level
        )

        print(
            "TARGET:",
            volume_target
        )

        used_titles = set()

        # =============================================
        # OBJECTIVES
        # =============================================

        primary_objectives = (

            self.objective_selector
            .get_primary_objectives(
                specialist
            )
        )

        activation_objectives = (

            self.objective_selector
            .get_activation_objectives(
                specialist
            )
        )

        speed_objectives = []

        if specialist in [

            "sprint",
            "middle_distance",
            "im"

        ]:

            speed_objectives = (

                self.objective_selector
                .get_speed_objectives(
                    specialist
                )
            )

        # =============================================
        # WARMUP
        # =============================================

        warmup = (

            self.block_builder.build(

                objective=
                "general_activation",

                category=
                "warmup",

                age=age,

                used_titles=
                used_titles,

                max_intensity=4,

                max_volume=1000,

                limit=1
            )
        )

        # =============================================
        # PRESET
        # =============================================

        preset = (

            self.block_builder.build(

                objective=
                "aerobic_technical",

                category=
                "preset",

                age=age,

                used_titles=
                used_titles,

                max_intensity=5,

                max_volume=1000,

                limit=1
            )
        )

        # =============================================
        # ACTIVATION
        # =============================================

        activation = []

        for objective in activation_objectives:

            remaining = (

                self.calculate_remaining_volume(

                    volume_target,

                    [
                        warmup,
                        preset,
                        activation
                    ]
                )
            )

            activation.extend(

                self.block_builder.build(

                    objective=objective,

                    category="warmup",

                    age=age,

                    used_titles=
                    used_titles,

                    max_intensity=8,

                    max_volume=min(
                        600,
                        remaining
                    ),

                    limit=1
                )
            )

        # =============================================
        # MAIN SET
        # =============================================

        main_set = []

        for objective in primary_objectives:

            current_blocks = [

                warmup,
                preset,
                activation,
                main_set
            ]

            remaining = (

                self.calculate_remaining_volume(

                    volume_target,

                    current_blocks
                )
            )

            candidates = (

                self.block_builder
                .build_candidates(

                    objective=
                    objective,

                    category=
                    "main_set",

                    used_titles=
                    used_titles,

                    max_intensity=10,

                    max_volume=
                    remaining
                )
            )

            if candidates:

                selected = (
                    candidates[0]
                )

                used_titles.add(

                    selected[
                        "title"
                    ].lower()
                )

                main_set.append(
                    selected
                )

        # =============================================
        # SPEED SET
        # =============================================
        if not allow_speed:

          speed_set = []

        else:

         speed_set = []

         for objective in speed_objectives:

            remaining = (

                self.calculate_remaining_volume(

                    volume_target,

                    [
                        warmup,
                        preset,
                        activation,
                        main_set,
                        speed_set
                    ]
                )
            )

            candidates = (

                self.block_builder
                .build_candidates(

                    objective=
                    objective,

                    category=
                    "speed",

                    used_titles=
                    used_titles,

                    max_intensity=10,

                    max_volume=min(
                        600,
                        remaining
                    )
                )
            )

            if candidates:

                selected = (
                    candidates[0]
                )

                used_titles.add(

                    selected[
                        "title"
                    ].lower()
                )

                speed_set.append(
                    selected
                )

                break

        # =============================================
        # RECOVERY
        # =============================================

        remaining = (

            self.calculate_remaining_volume(

                volume_target,

                [
                    warmup,
                    preset,
                    activation,
                    main_set,
                    speed_set
                ]
            )
        )

        recovery = (

            self.block_builder.build(

                objective=
                "recovery",

                age=age,

                used_titles=
                used_titles,

                max_intensity=2,

                max_volume=min(
                    400,
                    remaining
                ),

                limit=1
            )
        )

        # =============================================
        # ALL EXERCISES
        # =============================================

        all_exercises = []

        for block in [

            warmup,
            preset,
            activation,
            main_set,
            speed_set,
            recovery
        ]:

            all_exercises.extend(
                block
            )

        # =============================================
        # METRICS
        # =============================================

        total_volume = (

            self.fatigue_manager
            .calculate_volume(
                all_exercises
            )
        )

        total_cns = (

            self.fatigue_manager
            .calculate_cns_load(
                all_exercises
            )
        )

        average_intensity = (

            self.fatigue_manager
            .calculate_average_intensity(
                all_exercises
            )
        )

        fatigue_state = (

            self.fatigue_manager
            .get_fatigue_state(
                total_cns
            )
        )

        # =============================================
        # SESSION IDENTITY
        # =============================================

        session_identity = (
            "_".join(
                primary_objectives
            )
        )

        # =============================================
        # FINAL RESPONSE
        # =============================================
        

        print(
            "FINAL VOLUME:",
            total_volume
        )


        return {

            "session_identity":
            session_identity,

            "readiness":
            readiness_level,

            "metrics": {

                "total_volume":
                total_volume,

                "total_cns":
                total_cns,

                "average_intensity":
                average_intensity,

                "fatigue_state":
                fatigue_state
            },

            "session": {

                "warmup":
                warmup,

                "preset":
                preset,

                "activation":
                activation,

                "main_set":
                main_set,

                "speed_set":
                speed_set,

                "recovery":
                recovery
            }
        }
