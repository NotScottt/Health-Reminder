from win10toast import ToastNotifier
import datetime
import time

toast = ToastNotifier()

current_date = datetime.datetime.now()
year, week_num, day_of_week = current_date.isocalendar()

Startpunkt = True
counter_til_stop = 0


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



while Startpunkt:
    if counter_til_stop == 7 or current_date.hour == 16:
        Startpunkt = False
        toast.show_toast(
            "Hinweis",
            "Script wird beendet. Schönen Feierabend!",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
        )
        print(f"Counter beendet nach: {counter_til_stop} Stunden!")

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
            print(f"Der Timer für die Pausen geht jetzt los! Nächste Pause um 0{new_start}:{start_minute}. ({counter_til_stop})")
        
        else:
            toast.show_toast(
            "Hinweis",
            f"Der Timer für die Pausen geht jetzt los! Nächste Pause um {new_start}:{start_minute}.",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
            )
            counter_til_stop = counter_til_stop + 1
            print(f"Der Timer für die Pausen geht jetzt los! Nächste Pause um {new_start}:{start_minute}. ({counter_til_stop})")
        time.sleep(1)

    else:
        new_start = int(new_start) + 1
        if len(str(new_start)) == 1:
            toast.show_toast(
            "Hinweis",
            f"Du solltest kurz aufstehen und eine Pause machen! Nächste Pause um 0{new_start}:{start_minute}.",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
            )
            counter_til_stop = counter_til_stop + 1
            print(f"Du solltest kurz aufstehen und eine Pause machen! Nächste Pause um 0{new_start}:{start_minute}. ({counter_til_stop})")

        else:
            toast.show_toast(
            "Hinweis",
            f"Du solltest kurz aufstehen und eine Pause machen! Nächste Pause um {new_start}:{start_minute}.",
            duration = 20,
            icon_path = "health.ico",
            threaded = True,
            )
            counter_til_stop = counter_til_stop + 1
            print(f"Du solltest kurz aufstehen und eine Pause machen! Nächste Pause um {new_start}:{start_minute}. ({counter_til_stop})")
        time.sleep(1)