def filter_already_used_exercises(
    exercises,
    recent_sessions
):

    used_titles = []

    for session in recent_sessions:

        blocks = session.get(
            "blocks",
            []
        )

        for block in blocks:

            title = block.get(
                "title"
            )

            if title:

                used_titles.append(
                    title
                )

    filtered = []

    for ex in exercises:

        if ex.title not in used_titles:

            filtered.append(ex)

    # fallback
    if len(filtered) == 0:

        return exercises

    return filtered