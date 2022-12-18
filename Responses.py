import random
import json
import re


def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)

responses_data = load_json("bot.json")


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("good", "nice", "great"):
        return "hehe..."
    if user_message in ("who are you?", "who are you", "you?"):
        return ("Im Miles,and you are?")
    if user_message in ("Im lincia", "lincia narcis", "matlin", "inchamaru" "lincia matthew", "lincha", "linchamaru", "inchie", "lincia"):
        return "Oh,Im Glad meeting you,Lincia"
    if user_message in ("Im matthew", "matthew", "matthewlynn", "matt", "lynn", "maddy"):
        return "Oh,Im Glad meeting you,Matthew"
    if user_message in ("goodnight miles","good night miles"):
        return "Good night mate!, Sleep well"
    if user_message in ("Movies list"):
       return

    split_message = re.split(r"\s+|[,;?!.-]\s*", user_message.lower())
    score_list = []

    for response in responses_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if user_message == "":
        return "Please type something so we can chat :)"

    if best_response != 0:
        return responses_data[response_index]["bot_response"]

    if user_message in ("goodmorning","good morning","morning","gm"):
        random_list = [
            """Write it on your heart that every day is the best day in the year. – Ralph Waldo Emerson.
            Bright morning to you.CHEERS!!!""",
            """Every morning, I wake up saying, 'I’m still alive, a miracle.' And so I keep on pushing.-Jim Carrey.
            So give it a shot. Have a Great Morning!.""",
            """"When you arise in the morning, think of what a precious privilege it is to be alive, to breathe, to think, to enjoy, to love.” – Marcus Aurelius
            So, Have a Wonderful Morning! and a Great day""",
            """Smile in the mirror. Do that every morning and you’ll start to see a big difference in your life.– Yoko Ono
            So, smile and spread postivity. Good morning""",
            """If you get up in the morning and think the future is going to be better, it is a bright day. Otherwise, it’s not. – Elon Musk
             GoodMorning!""",
        ]
        list_count = len(random_list)
        random_item = random.randrange(list_count)
        return random_list[random_item]
    return(sample_responses())











