#coding
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:  # Scores 70 or lower
        student_grades[student] = "Fail"

print(student_grades)

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# print lille
print(travel_log["France"][1]) #to print lille

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2]) #will appear C and D as 0 is A, 1 is B, 2 is nested C and D
print(nested_list[2][1]) #will print D, 2 is the nested and then 1 is the inside of the nested list

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][2])

# Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
# answer
print(order["main"][2][0]) # [2] accesses the value with key 2, [0] gets the first item from the list

#auction

# Ask the user for some inputs

# import art
# print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
