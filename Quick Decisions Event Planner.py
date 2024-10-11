#task 1 code correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#task 2 Venue selection
attendees = int(input("Enter number of attendees: "))
if attendees > 100:
    venue = "large hall"
    audio_system = "surround sound"
    print(venue, audio_system)
else:
    venue = "conference room"
    audio_system = "basic system"
    print(venue, audio_system)

#task3
attendees = int(input("Enter number of attendees: "))
vegetarian= input("Are you vegetarian? (yes/no): ")
if attendees > 100:
    if vegetarian == "yes":
        venue = "large hall"
        audio_system = "surround sound"
        print("veggie delight caterers", venue, audio_system)
    else:
        venue = "large hall"
        audio_system = "surround sound"
        print("gourmet meal caterers", venue, audio_system)

else:
    if vegetarian == "no":
        venue = "conference room"
        audio_system = "basic system"
        print("gourmet meal caterers", venue, audio_system)
    else:
        venue = "conference room"
        audio_system = "basic system"
        print("veggie delight caterers", venue, audio_system)
