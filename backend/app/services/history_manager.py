from app.models.training_history import (
    TrainingHistory
)


# =========================
# SAVE TRAINING SESSION
# =========================

def save_training_session(
    db,
    analysis,
    fatigue_memory,
    energy_scores,
    week_number,
    stroke,
    session_type
):

    session = TrainingHistory(

        week_number=week_number,

        training_load=analysis[
            "training_load"
        ],

        fatigue_level=fatigue_memory[
            "fatigue_level"
        ],

        fatigue_score=fatigue_memory[
            "fatigue_score"
        ],

        high_cns_blocks=analysis[
            "high_cns_blocks"
        ],

        high_intensity_load=energy_scores[
            "high_intensity_load"
        ],

        session_type=session_type,

        stroke=stroke
    )

    db.add(session)

    db.commit()

    db.refresh(session)

    return session


# =========================
# GET RECENT SESSIONS
# =========================

def get_recent_sessions(
    db,
    limit=7
):

    sessions = db.query(
        TrainingHistory
    ).order_by(
        TrainingHistory.id.desc()
    ).limit(limit).all()

    results = []

    for s in sessions:

        results.append({

            "id":
            s.id,

            "week_number":
            s.week_number,

            "training_load":
            s.training_load,

            "fatigue_level":
            s.fatigue_level,

            "fatigue_score":
            s.fatigue_score,

            "high_cns_blocks":
            s.high_cns_blocks,

            "high_intensity_load":
            s.high_intensity_load,

            "session_type":
            s.session_type,

            "stroke":
            s.stroke
        })

    return results


# =========================
# GET TOTAL WEEK LOAD
# =========================

def get_week_load(
    db,
    week_number
):

    sessions = db.query(
        TrainingHistory
    ).filter(

        TrainingHistory.week_number
        == week_number

    ).all()

    total_load = 0

    for s in sessions:

        total_load += (
            s.training_load or 0
        )

    return {

        "week_number":
        week_number,

        "weekly_training_load":
        total_load,

        "session_count":
        len(sessions)
    }


# =========================
# GET CNS LOAD
# =========================

def get_recent_cns_load(
    db,
    limit=5
):

    sessions = db.query(
        TrainingHistory
    ).order_by(
        TrainingHistory.id.desc()
    ).limit(limit).all()

    total_cns = 0

    for s in sessions:

        total_cns += (
            s.high_cns_blocks or 0
        )

    return {

        "recent_cns_load":
        total_cns,

        "sessions_analyzed":
        len(sessions)
    }


# =========================
# GET HIGH INTENSITY DAYS
# =========================

def get_high_intensity_frequency(
    db,
    limit=7
):

    sessions = db.query(
        TrainingHistory
    ).order_by(
        TrainingHistory.id.desc()
    ).limit(limit).all()

    high_intensity_days = 0

    for s in sessions:

        if (
            s.high_intensity_load
            and
            s.high_intensity_load > 5000
        ):

            high_intensity_days += 1

    return {

        "high_intensity_days":
        high_intensity_days,

        "sessions_analyzed":
        len(sessions)
    }