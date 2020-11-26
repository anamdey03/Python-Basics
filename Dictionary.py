# Dictionary has key value pairs and it's mutable in nature. We use the curly brackets to declare a dictionary

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_conversions["Feb"])
print(month_conversions.get("Nov"))
print(month_conversions.get("Luv", "Not a valid key"))
