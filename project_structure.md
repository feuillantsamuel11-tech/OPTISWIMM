# OPTISWIMM PROJECT STRUCTURE

├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── athlete_routes.py
│   │   │   ├── generate_macrocycle.py
│   │   │   ├── generate_mesocycle.py
│   │   │   ├── generate_microcycle.py
│   │   │   ├── generate_season.py
│   │   │   ├── generate_session.py
│   │   │   └── monitoring.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   └── Nouveau Fichier source Python.py
│   │   ├── generators
│   │   │   └── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── exercise.py
│   │   │   ├── exercise_backup.py
│   │   │   ├── training_context.py
│   │   │   ├── training_history.py
│   │   │   └── zone.py
│   │   ├── routes
│   │   │   ├── __init__.py
│   │   │   ├── exercise_routes.py
│   │   │   ├── generator_routes.py
│   │   │   ├── init_routes.py
│   │   │   └── zone_routes.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   ├── athlete.py
│   │   │   ├── exercise_schema.py
│   │   │   ├── generator_schema.py
│   │   │   ├── readiness.py
│   │   │   ├── season_request.py
│   │   │   ├── session_request.py
│   │   │   ├── session_response.py
│   │   │   └── zone_schema.py
│   │   ├── services
│   │   │   ├── planner
│   │   │   ├── session_engine
│   │   │   │   ├── __init__.py
│   │   │   │   ├── block_builder.py
│   │   │   │   ├── block_builder_backup.py
│   │   │   │   ├── exercise_ranker.py
│   │   │   │   ├── fatigue_manager.py
│   │   │   │   ├── objective_selector.py
│   │   │   │   ├── readiness_manager.py
│   │   │   │   ├── recovery_manager.py
│   │   │   │   ├── session_variation.py
│   │   │   │   └── specialist_manager.py
│   │   │   ├── __init__.py
│   │   │   ├── adaptive_session_rebuilder.py
│   │   │   ├── adaptive_training_orchestrator.py
│   │   │   ├── athlete_monitoring.py
│   │   │   ├── athlete_profile_engine.py
│   │   │   ├── competition_engine.py
│   │   │   ├── constraint_engine.py
│   │   │   ├── database_cleanup_engine.py
│   │   │   ├── diversity_engine.py
│   │   │   ├── duplication_manager.py
│   │   │   ├── dynamic_block_builder.py
│   │   │   ├── dynamic_thresholds.py
│   │   │   ├── energy_scoring.py
│   │   │   ├── energy_system_manager.py
│   │   │   ├── exercise_relationship_engine.py
│   │   │   ├── exercise_scoring.py
│   │   │   ├── exercise_scoring_backup.py
│   │   │   ├── exercise_scoring_engine.py
│   │   │   ├── exercise_selector.py
│   │   │   ├── fatigue_engine.py
│   │   │   ├── fatigue_manager.py
│   │   │   ├── fatigue_memory_engine.py
│   │   │   ├── history_manager.py
│   │   │   ├── import_exercises.py
│   │   │   ├── intelligent_session_builder.py
│   │   │   ├── intelligent_session_builder_v10.py
│   │   │   ├── intelligent_session_builder_v10_1_STABLE.py
│   │   │   ├── load_validator.py
│   │   │   ├── macrocycle_engine.py
│   │   │   ├── mesocycle_engine.py
│   │   │   ├── microcycle_builder.py
│   │   │   ├── microcycle_engine.py
│   │   │   ├── microcycle_planner.py
│   │   │   ├── objective_normalizer_engine.py
│   │   │   ├── performance_prediction_engine.py
│   │   │   ├── periodization_engine.py
│   │   │   ├── physiological_progression_engine.py
│   │   │   ├── profile_thresholds.py
│   │   │   ├── progression_engine.py
│   │   │   ├── race_distance_engine.py
│   │   │   ├── race_specialization_engine.py
│   │   │   ├── readiness_engine.py
│   │   │   ├── replacement_engine.py
│   │   │   ├── replacement_profiles.py
│   │   │   ├── season_planner.py
│   │   │   ├── semantic_training_preservation.py
│   │   │   ├── session_builder.py
│   │   │   ├── session_coherence_engine.py
│   │   │   ├── session_generator_v2.py
│   │   │   ├── session_identity_engine.py
│   │   │   ├── session_optimizer.py
│   │   │   ├── session_planner.py
│   │   │   ├── session_serializer.py
│   │   │   ├── session_validator.py
│   │   │   ├── swimmer_profiles.py
│   │   │   ├── training_distribution_engine.py
│   │   │   └── training_memory.py
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   ├── data
│   │   └── exercises
│   │       ├── aerobic_foundation.json
│   │       ├── cooldown.json
│   │       ├── cooldown_plus.json
│   │       ├── kick.json
│   │       ├── lactate.json
│   │       ├── max_velocity.json
│   │       ├── mobility.json
│   │       ├── neural_speed.json
│   │       ├── parasympathetic.json
│   │       ├── preset.json
│   │       ├── pull.json
│   │       ├── race_activation.json
│   │       ├── race_pace.json
│   │       ├── recovery_plus.json
│   │       ├── speed_activation.json
│   │       ├── sprint.json
│   │       ├── technical_skill.json
│   │       ├── technique.json
│   │       ├── threshold.json
│   │       ├── vo2.json
│   │       └── warmup.json
│   ├── exercise_library
│   │   ├── adaptive_recovery
│   │   │   └── adaptive_recovery.json
│   │   ├── aerobic
│   │   │   └── aerobic.json
│   │   ├── aerobic_ladder
│   │   │   └── aerobic_ladder.json
│   │   ├── aerobic_power
│   │   │   └── aerobic_power.json
│   │   ├── aerobic_technical
│   │   │   └── aerobic_technical.json
│   │   ├── age_groups
│   │   │   ├── agegroup_10_12.json
│   │   │   ├── agegroup_13_15.json
│   │   │   ├── agegroup_16_18.json
│   │   │   ├── elite.json
│   │   │   └── senior.json
│   │   ├── AI_constraints
│   │   │   ├── cns_constraints.json
│   │   │   ├── compatibility_constraints.json
│   │   │   ├── fatigue_constraints.json
│   │   │   ├── lactate_constraints.json
│   │   │   └── recovery_constraints.json
│   │   ├── altitude_hypoxic
│   │   │   └── altitude_hypoxic.json
│   │   ├── competition_phase
│   │   │   ├── competition.json
│   │   │   ├── overload.json
│   │   │   ├── recovery_phase.json
│   │   │   ├── taper.json
│   │   │   └── transition_phase.json
│   │   ├── competition_simulation
│   │   │   └── competition_simulation.json
│   │   ├── cooldown
│   │   │   └── cooldown.json
│   │   ├── drill
│   │   │   └── drill.json
│   │   ├── dryland
│   │   │   └── dryland.json
│   │   ├── IM
│   │   │   └── im.json
│   │   ├── injury_prevention
│   │   │   ├── knee_breastroke.json
│   │   │   ├── lower_back.json
│   │   │   ├── scapular_control.json
│   │   │   └── shoulder_protection.json
│   │   ├── kick
│   │   │   └── kick.json
│   │   ├── lactate
│   │   │   └── lactate.json
│   │   ├── mental_pacing
│   │   │   └── mental_pacing.json
│   │   ├── microdose_elite
│   │   │   └── microdose_elite.json
│   │   ├── open_water
│   │   │   └── open_water.json
│   │   ├── pull
│   │   │   └── pull.json
│   │   ├── race_pace
│   │   │   └── race_pace.json
│   │   ├── race_pace_systems
│   │   │   └── race_pace_systems.json
│   │   ├── recovery
│   │   │   └── recovery.json
│   │   ├── resistance_power
│   │   │   └── resistance _power.json
│   │   ├── specialists
│   │   │   ├── distance_specialist.json
│   │   │   ├── im_specialist.json
│   │   │   ├── middle_distance.json
│   │   │   ├── open_water_specialist.json
│   │   │   └── sprint_specialist.json
│   │   ├── speed
│   │   │   └── speed.json
│   │   ├── speed_technical
│   │   │   └── speed_technical.json
│   │   ├── starts_turns
│   │   │   └── starts_turns.json
│   │   ├── starts_turns_underwater
│   │   │   ├── breakout.json
│   │   │   ├── starts.json
│   │   │   ├── turns.json
│   │   │   └── underwater.json
│   │   ├── stroke_specialist
│   │   │   └── stroke_specialist.json
│   │   ├── stroke_specialization
│   │   │   ├── backstroke.json
│   │   │   ├── breastroke.json
│   │   │   ├── butterfly.json
│   │   │   └── freestyle.json
│   │   ├── tempo_frequency
│   │   │   └── tempo_frequency.json
│   │   ├── threshold
│   │   │   └── threshold.json
│   │   ├── threshold_control
│   │   │   └── threshold_control.json
│   │   ├── vo2
│   │   │   └── vo2.json
│   │   └── warmup
│   │       └── warmup.json
│   ├── scripts
│   │   ├── generate_aerobic.py
│   │   ├── generate_cooldown.py
│   │   ├── generate_dryland.py
│   │   ├── generate_im.py
│   │   ├── generate_lactate.py
│   │   ├── generate_preset.py
│   │   ├── generate_race_pace.py
│   │   ├── generate_speed.py
│   │   ├── generate_starts.py
│   │   ├── generate_threshold.py
│   │   ├── generate_turns.py
│   │   ├── generate_underwater.py
│   │   ├── generate_warmup.py
│   │   └── import_library.py
│   ├── series_json
│   │   ├── elite_sets_pack_01.json
│   │   ├── lactate_pack_01.json
│   │   ├── optiswimm_120_exercises.json
│   │   ├── race_pace_1500_pack_01.json
│   │   ├── race_pace_pack_01.json
│   │   ├── race_pace_pack_02.json
│   │   ├── start_turn_pack_01..json
│   │   ├── threshold_pack_01.json
│   │   ├── underwater_pack_01.json
│   │   ├── vo2_distance_pack_01.json
│   │   ├── vo2_distance_pack_02.json
│   │   ├── vo2_new.json
│   │   └── vo2_pack_01.json
│   ├── series_json_v2
│   ├── sql
│   │   ├── cooldown.sql
│   │   ├── dryland.sql
│   │   ├── lactate.sql
│   │   ├── preset.sql
│   │   ├── race-pace.sql
│   │   ├── race_pace.sql
│   │   ├── speed.sql
│   │   ├── starts.sql
│   │   ├── threshold.sql
│   │   ├── turns.sql
│   │   ├── underwater.sql
│   │   └── warmup.sql
│   ├── .env
│   ├── app_backup.py
│   ├── app_v4_recovery.py
│   ├── backend_architecture.txt
│   ├── cleanup_database.py
│   ├── competition_planner.py
│   ├── create_tables.py
│   ├── exercise_scoring.py
│   ├── import_exercises.py
│   ├── import_json.py
│   ├── intelligent_session_builder_v10.py
│   ├── macrocycle_engine.py
│   ├── mesocycle_engine.py
│   ├── normalize_objectives.py
│   ├── python audit_and_import_uploaded.py
│   ├── recovered_builder.py
│   ├── requirements.txt
│   ├── streamlit_app.py
│   ├── test_fatigue_memory.py
│   ├── training_phase_engine.py
│   ├── v95.txt
│   └── v95_full.txt
├── frontend
│   ├── public
│   │   ├── favicon.svg
│   │   └── icons.svg
│   ├── series_json
│   │   ├── adaptive_recovery
│   │   │   └── adaptive_recovery.json
│   │   ├── aerobic
│   │   │   └── aerobic.json
│   │   ├── aerobic_ladder
│   │   │   └── aerobic_ladder.json
│   │   ├── aerobic_power
│   │   │   └── aerobic_power.json
│   │   ├── aerobic_technical
│   │   │   └── aerobic_technical.json
│   │   ├── age_groups
│   │   │   ├── agegroup_10_12.json
│   │   │   ├── agegroup_13_15.json
│   │   │   ├── agegroup_16_18.json
│   │   │   ├── elite.json
│   │   │   └── senior.json
│   │   ├── altitude_hypoxic
│   │   │   └── altitude_hypoxic.json
│   │   ├── competition_phase
│   │   │   ├── competition.json
│   │   │   ├── overload.json
│   │   │   ├── recovery_phase.json
│   │   │   ├── taper.json
│   │   │   └── transition_phase.json
│   │   ├── competition_simulation
│   │   │   └── competition_simulation.json
│   │   ├── cooldown
│   │   │   └── cooldown.json
│   │   ├── drill
│   │   │   └── drill.json
│   │   ├── dryland
│   │   │   └── dryland.json
│   │   ├── IM
│   │   │   └── im.json
│   │   ├── injury_prevention
│   │   │   ├── knee_breastroke.json
│   │   │   ├── lower_back.json
│   │   │   ├── scapular_control.json
│   │   │   └── shoulder_protection.json
│   │   ├── kick
│   │   │   └── kick.json
│   │   ├── lactate
│   │   │   └── lactate.json
│   │   ├── mental_pacing
│   │   │   └── mental_pacing.json
│   │   ├── microdose_elite
│   │   │   └── microdose_elite.json
│   │   ├── open_water
│   │   │   └── open_water.json
│   │   ├── pull
│   │   │   └── pull.json
│   │   ├── race_pace
│   │   │   └── race_pace.json
│   │   ├── race_pace_systems
│   │   │   └── race_pace_systems.json
│   │   ├── recovery
│   │   │   └── recovery.json
│   │   ├── resistance_power
│   │   │   └── resistance _power.json
│   │   ├── specialists
│   │   │   ├── distance_specialist.json
│   │   │   ├── im_specialist.json
│   │   │   ├── middle_distance.json
│   │   │   ├── open_water_specialist.json
│   │   │   └── sprint_specialist.json
│   │   ├── speed
│   │   │   └── speed.json
│   │   ├── speed_technical
│   │   │   └── speed_technical.json
│   │   ├── starts_turns
│   │   │   └── starts_turns.json
│   │   ├── starts_turns_underwater
│   │   │   ├── breakout.json
│   │   │   ├── starts.json
│   │   │   ├── turns.json
│   │   │   └── underwater.json
│   │   ├── stroke_specialist
│   │   │   └── stroke_specialist.json
│   │   ├── stroke_specialization
│   │   │   ├── backstroke.json
│   │   │   ├── breastroke.json
│   │   │   ├── butterfly.json
│   │   │   └── freestyle.json
│   │   ├── tempo_frequency
│   │   │   └── tempo_frequency.json
│   │   ├── threshold
│   │   │   └── threshold.json
│   │   ├── threshold_control
│   │   │   └── threshold_control.json
│   │   ├── vo2
│   │   │   └── vo2.json
│   │   └── warmup
│   │       └── warmup.json
│   ├── src
│   │   ├── assets
│   │   │   ├── hero.png
│   │   │   ├── react.svg
│   │   │   └── vite.svg
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── main.tsx
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── tools
│   ├── inspector.py
│   └── project_structure.py
├── architecture.txt
├── package-lock.json
├── package.json
├── project_structure.md
└── start_optiswimm.bat
