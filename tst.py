import subprocess

user_input = input("Enter a command to run: ")
subprocess.call(["python", "make_windrose.py", net, sid])

db_password = "mypassword123"  # ⚠️ كشف بيانات حساسة
