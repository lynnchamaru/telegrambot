from datetime import datetime


def random_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hi", "hello", "what's up", "sup", "hey",):
        return "Hey! yo!, How's it goin?"

    if user_message in ("who are you?", "who are you", "you?"):
        return ("Im Miles,and you are?")

    if user_message in ("Im lincia", "lincia narcis", "matlin", "inchamaru" "lincia matthew", "lincha", "linchamaru", "inchie","lincia"):
        return "Oh,Im Glad meeting you,Lincia"

    if user_message in ("Im matthew", "matthew", "matthewlynn", "matt", "lynn", "maddy"):
        return "Oh,Im Glad meeting you,Matthew"

    if user_message in ("Im shabarita", "shabari", "Im shabarita shakthi", "shakthi", "shabarita",):
        return "Oh,Im Glad meeting you,shabarita"

    if user_message in ("good","nice","great"):
        return "hehe..."

    if user_message in ("thanks","thankyou"):
        return "My pleasure"

    if user_message in ("goodnight miles","good night miles"):
        return "Good night mate!, Sleep well"

    if user_message in ("goodmorning miles","good morning miles","good morning","goodmorning","gm"):
        return "Ah! Sunshine,I hope your morning is as bright as you!, Have a great day."

    if user_message in ("goodevening miles","good evening miles","gudeve","gud eve","goodevening","good evening"):
        return "Evenings allow you to forget the bitter worries of the day and get ready for the sweet dreams of night. Evenings give you relaxation from a stressful day. Good evening!."

    if user_message in ("show me the movies", "movies to watch","movies list"):
        return ""

    if user_message in ("time", "what's the time now?", "do you know what time it is", "time?",):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return