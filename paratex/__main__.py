from datetime import date
from pathlib import Path

import pandas as pd
from extractor import extract_attendance, Session, fetch_sessions_from_interval

OUTPUT_PATH = Path(__file__).parent / 'output'


def main():
    sessions = fetch_sessions_from_interval(date(2011, 10, 15), date(2019, 10, 15))

    for month in sessions:
        for session in month:
            session_data = extract_attendance(session[0])
            dataframe = session_as_dataframe(session_data)
            path = OUTPUT_PATH / f"{dataframe.iloc[1, 3]}.csv"
            print('Saving', path, end='\r')
            dataframe.to_csv(path)


# Intended to be used later on the code. Will leave this here for utility
# purposes for now.
def session_as_dataframe(session: Session):
    observations = (
        (name, presence, justification, session.date)
        for name, (presence, justification) in session.attendance.items()
    )
    df = pd.DataFrame(observations)
    df = df.rename(
        {0: 'Nome', 1: 'Presenca', 2: 'Justificativa', 3: 'Data'},
        axis=1
    )
    return df


if __name__ == '__main__':
    main()
