from win10toast import ToastNotifier
import datetime
import time
import os
from tkinter import messagebox

toast = ToastNotifier()

current_date = datetime.datetime.now()
year, week_num, day_of_week = current_date.isocalendar()

username = os.getlogin() 
path = f"C:/Users/{username}/Desktop/WieLange"
path_to_file = f"C:/Users/{username}/Desktop/WieLange/solange.txt"

Startpunkt = True
counter_til_stop = 0

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
# t = 3
toast = ToastNotifier()

if not os.path.exists(path):
    os.makedirs(path)
    messagebox.showinfo("Info", f"Ein neuer Ordner wurde unter {path} erstellt.")

if len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 1:
    start_hour = f"0{current_date.hour}"
    start_minute = f"0{current_date.minute} Uhr"

    

elif len(str(current_date.hour)) == 2 and len(str(current_date.minute)) == 1:
    start_hour = f"{current_date.hour}"
    start_minute = f"0{current_date.minute} Uhr"

elif len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 2:
    start_hour = f"0{current_date.hour}"
    start_minute = f"{current_date.minute} Uhr"

else:
    start_hour = f"{current_date.hour}"
    start_minute = f"{current_date.minute} Uhr"

t = 3600

while Startpunkt:
    if counter_til_stop == 8 or current_date.hour == 16:
        Startpunkt = False
        toast.show_toast(
            "Hinweis",
            "Script wird beendet. Schönen Feierabend!",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
        )
        print(f"Counter beendet nach: {counter_til_stop} Stunden!")
        if not os.path.exists(path):
            with open(path_to_file, "a")as file:
                file.write(f"\n({new_start}:{start_minute}), Counter beendet nach: {counter_til_stop} Stunden!\n")
        else:
            with open(path_to_file, "a")as file:
                file.write(f"\n({new_start}:{start_minute}), Counter beendet nach: {counter_til_stop} Stunden!\n")
        

    elif counter_til_stop == 0:
        new_start = int(start_hour) + 1
        
        if len(str(new_start)) == 1:
            toast.show_toast(
            "Hinweis",
            f"Der Timer für die Pausen geht jetzt los! Nächste Pause um 0{new_start}:{start_minute}.",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
            )
            counter_til_stop = counter_til_stop + 1
            if not os.path.exists(path_to_file):
                with open(path_to_file, "a")as file:
                    file.write(f"({start_hour}:{start_minute}), Timer startet. Nächste Pause um 0{new_start}:{start_minute}.")
            else:
                if os.stat(path_to_file).st_size == 0:
                    with open(path_to_file, "a")as file:
                        file.write(f"({start_hour}:{start_minute}), Timer startet. Nächste Pause um 0{new_start}:{start_minute}.")
                else:
                    with open(path_to_file, "a")as file:
                        file.write(f"\n\n({start_hour}:{start_minute}), Timer startet. Nächste Pause um 0{new_start}:{start_minute}.")
            countdown(int(t))
        
        else:
            toast.show_toast(
            "Hinweis",
            f"Der Timer für die Pausen geht jetzt los! Nächste Pause um {new_start}:{start_minute}.",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
            )
            counter_til_stop = counter_til_stop + 1
            if not os.path.exists(path_to_file):
                with open(path_to_file, "a")as file:
                    file.write(f"({start_hour}:{start_minute}), Timer startet. Nächste Pause um {new_start}:{start_minute}.")
            else:
                if os.stat(path_to_file).st_size == 0:
                    with open(path_to_file, "a")as file:
                        file.write(f"({start_hour}:{start_minute}), Timer startet. Nächste Pause um {new_start}:{start_minute}.")
                else:
                    with open(path_to_file, "a")as file:
                        file.write(f"\n\n({start_hour}:{start_minute}), Timer startet. Nächste Pause um {new_start}:{start_minute}.")
                   
        countdown(int(t))
    
    else:
        new_start = int(new_start) + 1
        new_time = int(new_start) - 1
        run_seit = int(counter_til_stop) - 1
        print(f"Counter: {counter_til_stop}")
        if len(str(new_start)) == 1:
            toast.show_toast(
            "Hinweis",
            f"Eine Stunde ist rum, 5 min Augenpause. Nächste Pause um 0{new_start}:{start_minute}.",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
            )
            print("5min ab jetzt")

            counter_til_stop = counter_til_stop + 1
            counte_test = counter_til_stop - 1

            if not os.path.exists(path):
                with open(path_to_file, "a")as file:
                    file.write(f"({new_time}:{start_minute}), Stop! 5 Min pause ab jetzt. Nächste Pause um 0{new_start}:{start_minute}. Lauf seit {counte_test} Stunde/n")
            else:
                with open(path_to_file, "a")as file:
                    file.write(f"\n\n({new_time}:{start_minute}), Stop! 5 Min pause ab jetzt. Nächste Pause um 0{new_start}:{start_minute}. Lauf seit {counte_test} Stunde/n")
            countdown(int(300))

            
            countdown(int(t))
        
                   
        else:
            toast.show_toast(
            "Hinweis",
            f"Eine Stunde ist rum, 5 min Augenpause. Nächste Pause um 0{new_start}:{start_minute}.",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
            )
            print("5min ab jetzt")
            
            counter_til_stop = counter_til_stop + 1
            counte_test = counter_til_stop - 1

            if not os.path.exists(path):
                with open(path_to_file, "a")as file:
                    file.write(f"({new_time}:{start_minute}), Stop! 5 Min pause ab jetzt. Nächste Pause um {new_start}:{start_minute}. Lauf seit {counte_test} Stunde/n")
            else:
                with open(path_to_file, "a")as file:
                    file.write(f"\n\n({new_time}:{start_minute}), Stop! 5 Min pause ab jetzt. Nächste Pause um {new_start}:{start_minute}. Lauf seit {counte_test} Stunde/n")
            countdown(int(300))
        countdown(int(t))