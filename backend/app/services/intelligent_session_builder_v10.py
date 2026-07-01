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
from app.services.race_specialization_engine import (
    RaceSpecializationEngine
)
import random

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
        self.race_engine = (
    RaceSpecializationEngine()
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
            0,
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
        cns_fatigue = (

            athlete.get(
                "cns_fatigue",
                "low"
            )
        )

        if cns_fatigue == "high":
        
         if specialist != "sprint":

              allow_speed = False

              max_intensity = min(
                max_intensity,
                7
            )

        elif cns_fatigue == "moderate":

            max_intensity = min(
                max_intensity,
                8
            )

        print(
            "CNS FATIGUE BUILDER:",
            cns_fatigue
        )

        print(
            "ALLOW SPEED:",
            allow_speed
        )

        print(
            "MAX INTENSITY:",
            max_intensity
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
        distance_focus = athlete.get(
                    "distance_focus"
                )
        race_distance = athlete.get(
                            "race_distance",
                            400
                        )

        if distance_focus == "speed":

                primary_objectives = [
                    "speed"
                ]

        elif distance_focus == "race_pace":

                primary_objectives = [
                    "race_pace"
                ]

        elif distance_focus == "threshold":

                primary_objectives = [
                    "threshold_control"
                ]

        elif distance_focus == "aerobic":

                primary_objectives = [
                    "aerobic_power"
                ]
                

        print(
                    "DISTANCE FOCUS:",
                    distance_focus
            )

        print(
                    "RACE DISTANCE:",
                    race_distance
            
            )
            
        forced_focus = (
                athlete.get(
                    "daily_focus"
                )
            )
            
        print(
                "FORCED FOCUS:",
                forced_focus
            )

        
            
        mesocycle = (
                athlete.get(
                    "mesocycle_structure",
                    {}
                )
            )

        week_type = mesocycle.get(
                "week_type",
                "accumulation"
            )

        volume_multiplier = mesocycle.get(
                "volume_multiplier",
                1.0
            )

        intensity_multiplier = mesocycle.get(
                "intensity_multiplier",
                1.0
            )
            
        if week_type == "shock":

                athlete[
                    "objective_blocklist"
                ] = []

        elif week_type == "deload":

            athlete[
                "objective_blocklist"
            ] = []

            max_intensity = min(
                max_intensity,
                7
            )

            volume_target = int(
                volume_target * 0.70
            )

        max_intensity = min(
                10,
                int(
                    max_intensity *
                    intensity_multiplier
                )
            )

        print(
                "MESOCYCLE:",
                week_type
            )

        print(
                "VOLUME MULTIPLIER:",
                volume_multiplier
            )

        print(
                "INTENSITY MULTIPLIER:",
                intensity_multiplier
            )

        print(
                "ADJUSTED TARGET:",
                volume_target
            )

            
        if forced_focus:

                print(
                    "SPECIALIST:",
                    specialist
                )

                print(
                    "FORCED FOCUS:",
                    forced_focus
                )

                print(
                    "RACE DISTANCE:",
                    race_distance
                )

                primary_objectives = (

                    self.race_engine
                    .get_week_objectives(

                        specialist,

                        forced_focus,

                        race_distance
                    )
                ) 
        print(
                "WEEK OBJECTIVES RESULT:",
                primary_objectives
            )
        print(
                "AFTER WEEK OBJECTIVES:",
                primary_objectives
            )
        print(
                "PRIMARY BEFORE FILTER:",
                primary_objectives
            )
        objective_blocklist = (

                athlete.get(
                    "objective_blocklist",
                    []
                )
            )
        print(
                "OBJECTIVE BLOCKLIST:",
                objective_blocklist
            )
        primary_objectives = [

                obj

                for obj in primary_objectives

                if obj not in objective_blocklist
            ]
        print(
                "AFTER BLOCKLIST:",
                primary_objectives
            )

        if not primary_objectives:

            if forced_focus:

                if forced_focus == "threshold":

                    primary_objectives = [
                        "threshold_control"
                    ]

                elif forced_focus == "speed":

                    primary_objectives = [
                        "speed"
                    ]

                elif forced_focus == "race_pace":

                    primary_objectives = [
                        "race_pace"
                    ]

                elif forced_focus == "aerobic":

                    primary_objectives = [
                        "aerobic_power"
                    ]

                elif forced_focus == "recovery":

                    primary_objectives = [
                        "recovery"
                    ]

            else:

             primary_objectives = [
                 "recovery"
             ]

        print(
                "FILTERED OBJECTIVES:",
                primary_objectives
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

                    race_distance=race_distance,

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

                    race_distance=race_distance,

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

                        race_distance=race_distance,

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

            # DELoad protection

            if mesocycle == "deload":

                max_main_volume = int(
                    volume_target * 0.50
                )

            else:

                max_main_volume = int(
                    volume_target * 0.60
                )

            main_category = "main_set"

            if objective == "speed":

                main_category = "speed"

            candidates = (

                self.block_builder
           
                
                .build_candidates(

                    objective=objective,

                    category=main_category,

                    used_titles=used_titles,

                    race_distance=race_distance,

                    max_intensity=max_intensity,

                    max_volume=min(

                        remaining,

                        max_main_volume
                    )
                )
            )

            if  candidates:

                print(
                    "TOP 10 CANDIDATES:"
                )

                for c in candidates[:10]:

                    print(
                        c["title"],
                        c["volume"],
                        c.get("race_specificity")
                    )
            

            if not candidates:

                print(
                    "NO CANDIDATES"
                )

                continue

           

            selected = random.choice(
                candidates[:min(
                    5,
                    len(candidates)
                )]
            ) 

            print(
                "SELECTED:",
                selected["title"],
                selected["volume"],
                selected.get(
                    "race_specificity"
                )
            )

            used_titles.add(

                selected[
                    "title"
                ].lower()
            )

            main_set.append(
                selected
            )
            
            remaining = (

                self.calculate_remaining_volume(

                    volume_target,

                    [
                        warmup,
                        preset,
                        activation,
                        main_set
                    ]
                )
            )

            if remaining < 800:

                print(
                    "STOP MAIN SET"
                )

                break 
            
            while remaining > 1000:

                extra_candidates = (

                    self.block_builder
                
                    .build_candidates(

                        objective=objective,

                        category=main_category,

                        used_titles=used_titles,

                        race_distance=race_distance,

                        max_intensity=max_intensity,

                        max_volume=remaining
                    )
                )

                if not extra_candidates:

                    break

                extra = random.choice(

                    extra_candidates[
                        :min(
                            3,
                            len(extra_candidates)
                        )
                    ]
                )

                used_titles.add(
                    extra["title"].lower()
                )

                main_set.append(
                    extra
                )

                remaining = (

                    self.calculate_remaining_volume(

                        volume_target,

                        [
                            warmup,
                            preset,
                            activation,
                            main_set
                        ]
                    )
                )
                print(
                    "FINAL ALLOW SPEED:",
                    allow_speed
                )
        # =============================================
        # SPEED SET
        # =============================================

        speed_set = []

        if (

                allow_speed

                and

                "recovery"
                not in primary_objectives
            ):

            

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

                            objective=objective,

                            category="speed",

                            used_titles=used_titles,

                            race_distance=race_distance,

                            max_intensity=max_intensity,

                            max_volume=min(
                                1000,
                                remaining,
                                
                            )
                        )
                    )

                    if not candidates:

                        print(
                            "NO CANDIDATES FOR:",
                            objective
                        )

                        continue

                    selected = random.choice(

                        candidates[:min(
                            5,
                            len(candidates)
                        )]
                    )

                    print(
                            "SPEED SELECTED:",
                            selected["title"],
                            selected["volume"],
                            selected.get(
                                "race_specificity"
                            )
                        )

                    print(
                            "USED TITLES:",
                            used_titles
                        )

                    used_titles.add(
                            selected["title"].lower()
                        )

                    

                    speed_set.append(
                        selected
                    )
                    print(
                            "SPEED SET:",
                            speed_set
                        )
                    print(
                        "SPEED SET AFTER APPEND:",
                        len(speed_set)
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

                    race_distance=race_distance,

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
        # FILL REMAINING VOLUME
        # =============================================

        remaining = (

            self.calculate_remaining_volume(

                volume_target,

                [
                    warmup,
                    preset,
                    activation,
                    main_set,
                    speed_set,
                    recovery
                ]
            )
        )

        print(
            "REMAINING AFTER RECOVERY:",
            remaining
        )

        while remaining >= 400:

            filler = self.block_builder.build(

                objective="recovery",

                category="cooldown",

                used_titles=used_titles,

                race_distance=race_distance,

                max_intensity=2,

                max_volume=remaining,

                limit=1
            )

            if not filler:

                break

            recovery.extend(
                filler
            )

            remaining = (

                self.calculate_remaining_volume(

                    volume_target,

                    [
                        warmup,
                        preset,
                        activation,
                        main_set,
                        speed_set,
                        recovery
                    ]
                )
            )

            print(
                "REMAINING AFTER FILLER:",
                remaining
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
        