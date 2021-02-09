from datetime import date
from pathlib import Path

from .extractor import Session, extract_attendance, fetch_sessions_from_interval
from .join_parts import CSV, JOINED_PATH, PARTITIONED_PATH


def partitioned_process(sessions):
    PARTITIONED_PATH.mkdir(parents=True, exist_ok=True)
    for month in sessions:
        for session in month:
            session_id = session[0]
            session_data = extract_attendance(session_id)
            dataframe = session_as_dataframe(session_data)
            path = PARTITIONED_PATH / f"{session_data.title}.csv"
            print("Saving", path, end="\r")
            dataframe.save(path)


def joined_process(sessions, interval_begin, interval_end):
    JOINED_PATH.mkdir(parents=True, exist_ok=True)
    all_dfs = CSV(headers=("Nome", "Presenca", "Justificativa", "Data"), data=[])

    for month in sessions:
        for session in month:
            session_id = session[0]
            session_data = extract_attendance(session_id)
            dataframe = session_as_dataframe(session_data)
            print(f"Building {session_data.date}.csv", end="\r")
            all_dfs.data += dataframe.data

    all_dfs.save(JOINED_PATH / f"{interval_begin}_to_{interval_end}.csv")


def main(partitioned_mode=False):
    """
    partitioned_mode: True makes output splitted into a CSV file for each
    session, False joins sessions into a single CSV.
    """
    interval_begin = date(2014, 4, 22)
    interval_end = date(2015, 5, 15)

    sessions = fetch_sessions_from_interval(interval_begin, interval_end)

    if partitioned_mode:
        partitioned_process(sessions)
    else:
        joined_process(sessions, interval_begin, interval_end)


# Intended to be used later on the code. Will leave this here for utility
# purposes for now.
def session_as_dataframe(session: Session) -> CSV:
    observations = (
        (str(field) for field in (name, presence, justification, session.date))
        for name, (presence, justification) in session.attendance.items()
    )

    return CSV(
        headers=("Nome", "Presenca", "Justificativa", "Data"),
        data=list(observations),
    )


if __name__ == "__main__":
    main()
