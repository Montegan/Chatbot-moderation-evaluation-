from Moderations import moderateInput


def AskQuestions(user_input):
    return moderateInput(user_input)


response = AskQuestions(
    "I want to what is the price difference between the cheapest and the most expensive phone ")
