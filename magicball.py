import random
def magicball():
    responses=["of course!","its not very likely","perhaps in the near future","even i don't know that one","tough luck","It's certainly possible","The way shall be clear"]
    return f"The magic ball says {random.choice(responses)}"

print(magicball())


def weather_condition():
    print(f"The weather is fine in {autumn}")
    print(f"The weather is rough in {spring}")

autumn="spring"
spring="autumn"
weather_condition()

