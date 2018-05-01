print("Hello World!")

def cohort_member(proposed_member):
    cool_cohort_members=["Christiana", "Sam", "Louis", "Elizabeth"]
    if proposed_member in cool_cohort_members:
        print( "They're awesome!")
    else:
        print("Ewww.")
        
cohort_member("Ryan")

def weather(current_weather):
    acceptable_weather=["sunny", "cloudy", "sprinkles"]
    if current_weather in acceptable_weather:
        print("hello world, it's nice outside!")
    else:
        print("go home minnesota, you're drunk")
        
weather("sunny")