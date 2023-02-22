colors = ["red", "yellow", "black"]

print(colors[2])

print(type(colors))

colors.append("blue")
print(colors)

# insert at index 1.

colors.insert(1, "white")

print(colors)

# Remove Yellow

colors.remove("yellow")
print(colors)

colors.remove(colors[1])
print(colors)

# count
print(colors.count("white"))

print(len(colors))

# pop

var = colors.pop()
print(var)

# tuple
signal = ("1", "2", "3")
print(signal[1:3])
print(signal[0:])

# Dictionary - mobile automation

Marvel = {

    "Movie1": "Iron Man 1",
    "Movie2": "Avengers"
}

print(Marvel)
print(Marvel["Movie1"])

student_data = {

    "name": "gaurav",
    "mail": "abc@xyz",
    "marks": [13, 60, 97, 84, 56],
    "sports": {
        "indoor": "chess",
        "outdoor": "cricket"
    }
}

print(student_data)
print(student_data["marks"])

print(student_data["marks"][0])

print(student_data["sports"]["outdoor"])

#boolean

boo=True
print(type(boo))