def workshop():
    day1 = ["Alice@Email.com", "bob@email.com", "carol@email.com", "alice@email.com"]
    day2 = ["BOB@email.com", "dave@email.com", "Eve@email.com"]
    day3 = ["alice@email.com", "Eve@email.com", "frank@email.com", "BOB@email.com"]
    day1=set(email.lower() for email in day1)
    day2=set(email.lower() for email in day2)
    day3=set(email.lower() for email in day3)
    unique_all=day1|day2|day3
    print(len(unique_all))
    all_days=day1&day2&day3
    print(all_days)
    e_day1=day1-(day2|day3)
    e_day2=day2-(day1|day3)
    e_day3=day3-(day1|day2)
    print(f"the attendee who attended at day1:{e_day1}")
    print(f"the attendee who attended at day2:{e_day2}")
    print(f"the attendee who attended at day3:{e_day3}")
    print(f"{e_day1|e_day2|e_day3}")
    


workshop()