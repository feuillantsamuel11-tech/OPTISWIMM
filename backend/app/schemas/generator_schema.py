from pydantic import BaseModel


class SessionGenerateRequest(
    BaseModel
):

    # =========================
    # FILIÈRE PRINCIPALE
    # =========================

    zone: str

    # =========================
    # NAGE PRINCIPALE
    # =========================

    stroke: str

    # =========================
    # TYPE DE SÉANCE
    # =========================

    category: str

    # =========================
    # SEMAINE PLANIFICATION
    # =========================

    week_number: int

    # =========================
    # PROFIL NAGEUR
    # =========================

    swimmer_profile: str