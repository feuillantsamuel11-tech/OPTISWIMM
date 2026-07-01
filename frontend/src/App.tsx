
import { useState } from "react";
import axios from "axios";

const zoneColors: any = {

  Z1: "#38bdf8",
  Z2: "#22c55e",
  Z3: "#eab308",
  Z4: "#f97316",
  Z5: "#ef4444",
  Z6: "#a855f7",
  Z7: "#ec4899"
};

const cnsColors: any = {

  1: "#22c55e",
  2: "#eab308",
  3: "#ef4444"
};

function App() {

  const [session, setSession] =
  useState<any>(null);

  const generateSession =
  async () => {

    try {

      const response =
      await axios.post(

        "http://127.0.0.1:8000/api/generate-session",

        {

          athlete: {

            name: "Samuel",

            age: 18,

            specialist:
            "middle_distance"
          },

          readiness: {

            sleep_quality: 8,

            stress_level: 3,

            muscle_soreness: 2,

            motivation: 9,

            hrv_score: 8,

            fatigue_subjective: 3
          }
        }
      );

      setSession(
        response.data.data
      );

    } catch (error) {

      console.error(error);
    }
  };

  const renderExercises =
  (exercises: any[]) => {

    if (
      !exercises ||
      exercises.length === 0
    ) {

      return (
        <div className="empty">
          No exercises
        </div>
      );
    }

    return exercises.map(

      (
        ex: any,
        index: number
      ) => (

        <div
          key={index}
          className="exercise"
        >

          <div
            className="exerciseTop"
          >

            <h3>
              {ex.title}
            </h3>

            <div
              className="exerciseBadges"
            >

              <span
                className="zone"
                style={{
                  background:
                  zoneColors[
                    ex.zone
                  ]
                }}
              >
                {ex.zone}
              </span>

              <span
                className="cnsBadge"
                style={{
                  background:
                  cnsColors[
                    ex.cns
                  ]
                }}
              >
                CNS {ex.cns}
              </span>

            </div>

          </div>

          <div
            className="exerciseMetrics"
          >

            <div>
              <strong>
                {ex.volume}m
              </strong>

              <span>
                Volume
              </span>
            </div>

            <div>
              <strong>
                {ex.intensity}
              </strong>

              <span>
                Intensity
              </span>
            </div>

            <div>
              <strong>
                {ex.rest}s
              </strong>

              <span>
                Rest
              </span>
            </div>

          </div>

          <div className="exerciseInfo">

            <div>
              Energy:
              <strong>
                {" "}
                {ex.energy_system}
              </strong>
            </div>

            <div>
              Focus:
              <strong>
                {" "}
                {ex.focus}
              </strong>
            </div>

          </div>

        </div>
      )
    );
  };

  return (

    <div className="app">

      <div className="topbar">

        <div>

          <h1>
            OPTISWIMM Elite
          </h1>

          <p>
            Adaptive Swimming
            Intelligence Platform
          </p>

        </div>

        <button
          onClick={generateSession}
        >
          Generate Session
        </button>

      </div>

      <div className="dashboardGrid">

        <div className="leftPanel">

          <div className="heroCard">

            <div className="heroTop">

              <div>

                <div className="athleteName">
                  Samuel
                </div>

                <div className="athleteMeta">
                  Middle Distance ·
                  Elite Development
                </div>

              </div>

              <div className="readinessCircle">
                92
              </div>

            </div>

            <div className="statusRow">

              <div className="statusBadge">
                CNS Primed
              </div>

              <div className="statusBadge">
                Recovery Good
              </div>

              <div className="statusBadge">
                Race Phase
              </div>

            </div>

          </div>

          {session && (

            <div className="metricsGrid">

              <div className="metricCard">

                <span>
                  Volume
                </span>

                <strong>
                  {
                    session
                    .adaptive_session
                    .metrics
                    .total_volume
                  }m
                </strong>

              </div>

              <div className="metricCard">

                <span>
                  CNS
                </span>

                <strong>
                  {
                    session
                    .adaptive_session
                    .metrics
                    .total_cns
                  }
                </strong>

              </div>

              <div className="metricCard">

                <span>
                  Intensity
                </span>

                <strong>
                  {
                    session
                    .adaptive_session
                    .metrics
                    .average_intensity
                  }
                </strong>

              </div>

              <div className="metricCard">

                <span>
                  Fatigue
                </span>

                <strong>
                  {
                    session
                    .adaptive_session
                    .metrics
                    .fatigue_state
                  }
                </strong>

              </div>

            </div>
          )}

          {session && (

            <div className="mainSetCard">

              <div className="sectionTitle">
                MAIN SET
              </div>

              {
                renderExercises(

                  session
                  .adaptive_session
                  .session
                  .main_set
                )
              }

            </div>
          )}

        </div>

        <div className="rightPanel">

          {session && (

            <>

              <div className="card">

                <div className="sectionTitle">
                  Warmup
                </div>

                {
                  renderExercises(

                    session
                    .adaptive_session
                    .session
                    .warmup
                  )
                }

              </div>

              <div className="card">

                <div className="sectionTitle">
                  Activation
                </div>

                {
                  renderExercises(

                    session
                    .adaptive_session
                    .session
                    .activation
                  )
                }

              </div>

              <div className="card">

                <div className="sectionTitle">
                  Recovery
                </div>

                {
                  renderExercises(

                    session
                    .adaptive_session
                    .session
                    .recovery
                  )
                }

              </div>

            </>
          )}

        </div>

      </div>

    </div>
  );
}

export default App;

