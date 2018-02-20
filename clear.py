import sys
import sqlite3
def main():
    db = sqlite3.connect("data.db")
    c = db.cursor()
    l = sys.argv
    c.execute("UPDATE Attendance set Attend='No'")
    db.commit()
if __name__ == "__main__":
    main()
