import sys
import sqlite3
def main():
    try:
        db = sqlite3.connect("data.db")
        c = db.cursor()
        l = sys.argv
        c.execute("INSERT INTO Attendance VALUES(?,?)",(int(l[1]),""))
        c.execute("INSERT INTO login VALUES(?,?,?)",(int(l[1]),str(l[2]),str(l[3])))
        db.commit()
    except:
        return "false"
    return "true"
if __name__ == "__main__":
    x = main()
    print(x)
