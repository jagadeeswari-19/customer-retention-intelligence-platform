import shutil

SOURCE = "user_events.csv"
DEST = "data/raw/user_events.csv"

shutil.copy(SOURCE, DEST)

print("Dataset copied successfully")