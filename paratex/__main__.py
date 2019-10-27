import pandas as pd
from datetime import date
from extractor import extract_attendance, Session, fetch_sessions_from_interval

def main():
    attendances = []
    sessions = fetch_sessions_from_interval(date(2011, 10, 15), date(2019, 10, 15))
    
    for month in sessions:
        for session in month:
            session_data = extract_attendance(session[0])
            dataframe = session_as_dataframe(session_data)
            attendances.append(dataframe)

    for dataframe in attendances:
        dataframe.to_csv(f"output/{dataframe.iloc[1,3]}.csv")

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