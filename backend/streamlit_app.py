
from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="OPTISWIMM",
    layout="wide"
)

st.title("OPTISWIMM")
st.subheader("Swimming Performance Analytics Dashboard")

# =========================================================
# DATABASE CONNECTION
# =========================================================

engine = create_engine(
    "postgresql://postgres:admin@localhost/optiswimm_db"
)

# =========================================================
# ATHLETE FILTER
# =========================================================

athlete_query = """
SELECT first_name
FROM athletes
ORDER BY first_name;
"""

athlete_df = pd.read_sql(athlete_query, engine)

athlete_list = athlete_df["first_name"].tolist()

selected_athlete = st.selectbox(
    "Select Athlete",
    athlete_list
)

# =========================================================
# QUERY : VOLUME BY ZONE
# =========================================================

query_zone = f"""
SELECT
    z.code,
    SUM(ts.distance * ts.repetitions) AS volume
FROM training_sets ts
JOIN zones z
ON ts.zone_id = z.id
JOIN training_history th
ON ts.training_id = th.id
JOIN athletes a
ON th.athlete_id = a.id
WHERE a.first_name = '{selected_athlete}'
GROUP BY z.code
ORDER BY z.code;
"""

df_zone = pd.read_sql(query_zone, engine)

# =========================================================
# QUERY : VOLUME BY ATHLETE
# =========================================================

query_athlete = """
SELECT
    a.first_name,
    SUM(ts.distance * ts.repetitions) AS total_volume
FROM training_sets ts
JOIN training_history th
ON ts.training_id = th.id
JOIN athletes a
ON th.athlete_id = a.id
GROUP BY a.first_name
ORDER BY total_volume DESC;
"""

df_athlete = pd.read_sql(query_athlete, engine)

# =========================================================
# QUERY : WEEKLY LOAD
# =========================================================

query_load = f"""
SELECT
    week_number,
    SUM(session_score) AS weekly_load
FROM training_history th
JOIN athletes a
ON th.athlete_id = a.id
WHERE a.first_name = '{selected_athlete}'
GROUP BY week_number
ORDER BY week_number;
"""

df_load = pd.read_sql(query_load, engine)

# =========================================================
# QUERY : SESSION COUNT
# =========================================================

query_sessions = f"""
SELECT
    COUNT(*) AS total_sessions
FROM training_history th
JOIN athletes a
ON th.athlete_id = a.id
WHERE a.first_name = '{selected_athlete}';
"""

df_sessions = pd.read_sql(query_sessions, engine)

# =========================================================
# KPI CALCULATIONS
# =========================================================

total_volume = 0

if not df_zone.empty:
    total_volume = df_zone["volume"].sum()

total_sessions = int(df_sessions["total_sessions"][0])

total_load = 0
average_load = 0

if not df_load.empty:
    total_load = df_load["weekly_load"].sum()
    average_load = df_load["weekly_load"].mean()

# =========================================================
# KPI DISPLAY
# =========================================================

st.header("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Volume",
    f"{int(total_volume)} m"
)

col2.metric(
    "Sessions",
    total_sessions
)

col3.metric(
    "Total Load",
    int(total_load)
)

col4.metric(
    "Average Weekly Load",
    int(average_load)
)

# =========================================================
# ALERTS
# =========================================================

if average_load > 5000:
    st.warning("High training load detected")

if total_volume > 10000:
    st.warning("Very high training volume")

# =========================================================
# DISPLAY DATA TABLES
# =========================================================

st.header("Volume by Zone")

st.dataframe(df_zone)

st.header("Volume by Athlete")

st.dataframe(df_athlete)

st.header("Weekly Training Load")

st.dataframe(df_load)

# =========================================================
# CHART : VOLUME BY ZONE
# =========================================================

st.header("Zone Distribution")

fig1, ax1 = plt.subplots()

if not df_zone.empty:

    ax1.bar(
        df_zone["code"],
        df_zone["volume"]
    )

    ax1.set_xlabel("Zone")
    ax1.set_ylabel("Volume")
    ax1.set_title("Training Volume by Zone")

    st.pyplot(fig1)

# =========================================================
# CHART : VOLUME BY ATHLETE
# =========================================================

st.header("Athlete Volume")

fig2, ax2 = plt.subplots()

if not df_athlete.empty:

    ax2.bar(
        df_athlete["first_name"],
        df_athlete["total_volume"]
    )

    ax2.set_xlabel("Athlete")
    ax2.set_ylabel("Volume")
    ax2.set_title("Total Volume by Athlete")

    st.pyplot(fig2)

# =========================================================
# CHART : WEEKLY LOAD
# =========================================================

st.header("Weekly Load Evolution")

fig3, ax3 = plt.subplots()

if not df_load.empty:

    ax3.plot(
        df_load["week_number"],
        df_load["weekly_load"],
        marker="o"
    )

    ax3.set_xlabel("Week")
    ax3.set_ylabel("Load")
    ax3.set_title("Weekly Training Load")

    st.pyplot(fig3)

# =========================================================
# POLARIZATION ANALYSIS
# =========================================================

st.header("Training Polarization")

low_intensity = 0
high_intensity = 0

if not df_zone.empty:

    low_data = df_zone[
        df_zone["code"].isin(["Z1", "Z2"])
    ]["volume"]

    high_data = df_zone[
        df_zone["code"].isin(["Z5", "Z6", "Z7"])
    ]["volume"]

    low_intensity = low_data.sum()
    high_intensity = high_data.sum()

# Replace NaN by 0
if pd.isna(low_intensity):
    low_intensity = 0

if pd.isna(high_intensity):
    high_intensity = 0

polarization_df = pd.DataFrame({
    "Intensity": ["Low", "High"],
    "Volume": [low_intensity, high_intensity]
})

st.dataframe(polarization_df)

# Create pie chart only if volume exists
if (low_intensity + high_intensity) > 0:

    fig4, ax4 = plt.subplots()

    ax4.pie(
        polarization_df["Volume"],
        labels=polarization_df["Intensity"],
        autopct='%1.1f%%'
    )

    ax4.set_title("Training Polarization")

    st.pyplot(fig4)

else:

    st.info("No polarization data available")


# =========================================================
# RAW TRAINING HISTORY
# =========================================================

st.header("Training History")

query_history = f"""
SELECT
    th.id,
    a.first_name,
    th.week_number,
    th.session_type,
    th.training_load,
    th.session_score,
    th.duration_minutes,
    th.rpe,
    th.session_date
FROM training_history th
JOIN athletes a
ON th.athlete_id = a.id
WHERE a.first_name = '{selected_athlete}'
ORDER BY th.session_date;
"""

df_history = pd.read_sql(query_history, engine)

st.dataframe(df_history)

# =========================================================
# RAW TRAINING SETS
# =========================================================

st.header("Training Sets")

query_sets = f"""
SELECT
    a.first_name,
    z.code,
    ts.distance,
    ts.repetitions,
    ts.target_pace,
    ts.stroke,
    ts.intensity_note
FROM training_sets ts
JOIN training_history th
ON ts.training_id = th.id
JOIN athletes a
ON th.athlete_id = a.id
JOIN zones z
ON ts.zone_id = z.id
WHERE a.first_name = '{selected_athlete}';
"""

df_sets = pd.read_sql(query_sets, engine)

st.dataframe(df_sets)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")
# =========================================================
# COACH VIEW
# =========================================================

st.markdown("---")
st.header("Coach View")

query_session = """
SELECT
    title,
    session_type,
    objective,
    duration_minutes,
    total_volume,
    coach_notes
FROM session_templates
ORDER BY id
LIMIT 1;
"""

df_session = pd.read_sql(query_session, engine)

if not df_session.empty:

    session = df_session.iloc[0]

    st.subheader(session["title"])

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Duration",
        f"{session['duration_minutes']} min"
    )

    col2.metric(
        "Volume",
        f"{session['total_volume']} m"
    )

    col3.metric(
        "Type",
        session["session_type"]
    )

    st.success(
        f"Objective : {session['objective']}"
    )

    st.info(
        f"Coach Notes : {session['coach_notes']}"
    )

query_blocks = """
SELECT
    sb.block_order,
    sb.block_type,
    z.code,
    sb.repetitions,
    sb.distance,
    sb.sendoff,
    sb.target_pace,
    sb.stroke,
    sb.equipment,
    sb.instruction
FROM session_blocks sb
JOIN zones z
ON sb.zone_id = z.id
ORDER BY sb.block_order;
"""

df_blocks = pd.read_sql(query_blocks, engine)

st.markdown("## Session Blocks")

for _, row in df_blocks.iterrows():

    st.markdown("---")

    st.subheader(
        f"BLOC {row['block_order']} - {row['block_type'].upper()}"
    )

    st.write(
        f"**Set :** {row['repetitions']} x {row['distance']} m"
    )

    st.write(
        f"**Zone :** {row['code']}"
    )

    st.write(
        f"**Stroke :** {row['stroke']}"
    )

    st.write(
        f"**Sendoff :** {row['sendoff']}"
    )

    st.write(
        f"**Target Pace :** {row['target_pace']}"
    )

    st.write(
        f"**Equipment :** {row['equipment']}"
    )

    st.warning(
        f"Coach Instruction : {row['instruction']}"
    )


st.caption("OPTISWIMM V1 - Swimming Performance Analytics")

