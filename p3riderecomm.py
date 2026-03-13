drivers = [
 {"name":"Rahul","rating":4.8,"language":"Hindi"},
 {"name":"Amit","rating":4.5,"language":"English"}
]

users={"user1":{"preferred_language":"Hindi","budget":30}}

def book_ride(user_id,distance):
    user=users[user_id]

    price=distance*15
    ride="Mini" if price<user["budget"] else "Sedan"

    drivers_lang=[d for d in drivers if d["language"]==user["preferred_language"]]
    best=max(drivers_lang or drivers,key=lambda x:x["rating"])

    return ride,best["name"]

print(book_ride("user1",10))