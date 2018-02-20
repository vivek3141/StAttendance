import sys
import sqlite3
def main():
    try:
        db = sqlite3.connect("data.db")
        c = db.cursor()
        l = sys.argv
        c.execute("select password from login where ID="+str(l[1]))
        v = c.fetchall()
        if(str(v[0][0]) != str(l[3])):
            return "false"
        c.execute("UPDATE Attendance set Attend='Yes' where ID="+str(l[1]))
        db.commit()
        return "true"
    except:
        return "false"

if __name__ == "__main__":
    x = main()
    print(x)
