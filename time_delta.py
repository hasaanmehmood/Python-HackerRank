# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
#Constrainst:
# Input contains only valid timestamps.
# year <= 3000  

# Input Format
# The first line contains , the number of testcases.
# Each testcase contains  lines, representing time  and time .


import os
from datetime import datetime

# %a → abbreviated weekday name (Wed)
# %d → day of month (18)
# %b → abbreviated month name (Feb)
# %Y → 4-digit year (2026)
# %H:%M:%S → time (17:25:25)
# %z → UTC offset (like +0000, +0530)

FORMAT = "%a %d %b %Y %H:%M:%S %z"
MAX_YEAR = 3000

def time_delta(t1: str, t2: str) -> str:
    """
    Returns the absolute difference (in seconds) between two timestamps.
    Enforces the constraint: year <= 3000.
    """
    dt1 = datetime.strptime(t1, FORMAT)
    dt2 = datetime.strptime(t2, FORMAT)

    # Constraint: year <= 3000
    if dt1.year > MAX_YEAR or dt2.year > MAX_YEAR:
        raise ValueError("Year exceeds 3000")

    seconds = int(abs((dt1 - dt2).total_seconds()))
    return str(seconds)

if __name__ == "__main__":
    t = int(input().strip())

    with open(os.environ["OUTPUT_PATH"], "w") as f:
        for _ in range(t):
            t1 = input().strip()
            t2 = input().strip()
            f.write(time_delta(t1, t2) + "\n")