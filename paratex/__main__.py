import pandas as pd

from .extractor import extract_attendance, Session


def main():
    session = extract_attendance(1783)
    print(session.title)
    print(as_dataframe(session).head())


# Intended to be used later on the code. Will leave this here for utility
# purposes for now.
def as_dataframe(session: Session):
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
