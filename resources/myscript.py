# Create data for questions
questions_data = {
    'ID': list(range(1, 101)),
    'Question Content': [

        "What is 5 + 3?",
        "Solve for x: 2x + 3 = 7",
        "What is the square root of 16?",
        "If a rectangle has a length of 8 and a width of 3, what is its area?",
        "What is 12 divided by 4?",
        "What is 7 + 6?",
        "What is 9 - 4?",
        "What is 15 / 3?",
        "If a triangle has a base of 5 and a height of 4, what is its area?",
        "What is 6 x 3?",
        "What is 10 + 5?",
        "What is 20 - 10?",
        "What is 25 divided by 5?",
        "What is the product of 4 and 5?",
        "What is the sum of 10 and 15?",
        "What is the difference between 30 and 10?",
        "What is 7 times 3?",
        "What is 18 divided by 6?",
        "What is 20 minus 5?",
        "What is 12 + 8?",
        "If a square has a side length of 4, what is its area?",
        "What is 9 + 6?",
        "What is 15 - 5?",
        "What is 14 divided by 2?",
        "What is the sum of 11 and 9?",
        "What is the difference between 20 and 8?",
        "What is 8 times 2?",
        "What is 16 divided by 4?",
        "What is 24 - 6?",
        "What is 13 + 7?",
        "What is the product of 3 and 7?",
        "What is 30 divided by 3?",
        "What is the sum of 12 and 5?",
        "What is the difference between 25 and 5?",
        "What is 4 times 6?",
        "What is 21 divided by 7?",
        "What is 18 - 4?",
        "What is 11 + 10?",
        "If a circle has a radius of 3, what is its diameter?",
        "What is 9 times 4?",
        "What is 20 divided by 4?",
        "What is 14 + 8?",
        "What is the difference between 19 and 3?",
        "What is the product of 5 and 6?",
        "What is 28 divided by 4?",
        "What is the sum of 17 and 8?",
        "What is 15 minus 7?",
        "What is 6 times 4?",
        "What is 32 divided by 8?",
        "What is 20 + 9?",
        "What is the difference between 23 and 5?",
        "What is 3 times 9?",
        "What is 18 divided by 3?",
        "What is 11 + 12?",
        "What is 25 - 10?",
        "What is the product of 4 and 8?",
        "What is 24 divided by 3?",
        "What is the sum of 14 and 10?",
        "What is 19 minus 7?",
        "What is 5 times 5?",
        "What is 30 divided by 6?",
        "What is 13 + 9?",
        "What is the difference between 21 and 4?",
        "What is 2 times 7?",
        "What is 18 divided by 9?",
        "What is 16 - 8?",
        "What is 10 + 6?",
        "What is the product of 3 and 8?",
        "What is 27 divided by 3?",
        "What is the sum of 15 and 6?",
        "What is 22 minus 11?",
        "What is 5 times 4?",
        "What is 20 divided by 5?",
        "What is 17 + 7?",
        "What is the difference between 30 and 15?",
        "What is 4 times 5?",
        "What is 28 divided by 7?",
        "What is 18 - 6?",
        "What is 10 + 11?",
        "If a hexagon has a side length of 2, what is its perimeter?",
        "What is 9 times 3?",
        "What is 24 divided by 6?",
        "What is 14 + 5?",
        "What is the difference between 27 and 9?",
        "What is 7 times 2?",
        "What is 21 divided by 3?",
        "What is 12 - 6?",
        "What is 13 + 8?",
        "What is the product of 6 and 3?",
        "What is 30 divided by 5?",
        "What is the sum of 16 and 7?",
        "What is 20 minus 12?",
        "What is 2 times 9?",
        "What is 18 divided by 2?",
        "What is 15 - 5?",
        "What is 6 + 8?",
        "What is the product of 7 and 4?",
        "What is 35 divided by 5?",
        "What is the sum of 12 and 10?",
        "What is 25 minus 5?",
        "What is 8 times 5?",
        "What is 40 divided by 8?",
        "What is 50 minus 25?"
    ] * 2  # Repeat the list to ensure there are 100 unique questions
}
# Create data for ans
answers_data = {
    'ID': list(range(1, 101)),
    'Question ID': list(range(1, 101)),
    'Answer Content': [
        "8",                   # What is 5 + 3?
        "2",                   # Solve for x: 2x + 3 = 7
        "4",                   # What is the square root of 16?
        "24",                  # If a rectangle has a length of 8 and a width of 3, what is its area?
        "3",                   # What is 12 divided by 4?
        "13",                  # What is 7 + 6?
        "5",                   # What is 9 - 4?
        "5",                   # What is 15 / 3?
        "10",                  # If a triangle has a base of 5 and a height of 4, what is its area?
        "18",                  # What is 6 x 3?
        "15",                  # What is 10 + 5?
        "10",                  # What is 20 - 10?
        "5",                   # What is 25 divided by 5?
        "20",                  # What is the product of 4 and 5?
        "25",                  # What is the sum of 10 and 15?
        "20",                  # What is the difference between 30 and 10?
        "21",                  # What is 7 times 3?
        "3",                   # What is 18 divided by 6?
        "15",                  # What is 20 minus 5?
        "20",                  # What is 12 + 8?
        "16",                  # If a square has a side length of 4, what is its area?
        "15",                  # What is 9 + 6?
        "10",                  # What is 15 - 5?
        "7",                   # What is 14 divided by 2?
        "20",                  # What is the sum of 11 and 9?
        "12",                  # What is the difference between 20 and 8?
        "16",                  # What is 8 times 2?
        "4",                   # What is 16 divided by 4?
        "18",                  # What is 24 - 6?
        "20",                  # What is 13 + 7?
        "21",                  # What is the product of 3 and 7?
        "10",                  # What is 30 divided by 3?
        "17",                  # What is the sum of 12 and 5?
        "20",                  # What is the difference between 25 and 5?
        "24",                  # What is 4 times 6?
        "3",                   # What is 21 divided by 7?
        "14",                  # What is 18 - 4?
        "21",                  # What is 11 + 10?
        "6",                   # If a circle has a radius of 3, what is its diameter?
        "36",                  # What is 9 times 4?
        "5",                   # What is 20 divided by 4?
        "22",                  # What is 14 + 8?
        "16",                  # What is the difference between 19 and 3?
        "30",                  # What is the product of 5 and 6?
        "7",                   # What is 28 divided by 4?
        "25",                  # What is the sum of 17 and 8?
        "8",                   # What is 15 minus 7?
        "24",                  # What is 6 times 4?
        "4",                   # What is 32 divided by 8?
        "29",                  # What is 20 + 9?
        "18",                  # What is the difference between 23 and 5?
        "27",                  # What is 3 times 9?
        "6",                   # What is 18 divided by 3?
        "23",                  # What is 11 + 12?
        "15",                  # What is 25 - 10?
        "32",                  # What is the product of 4 and 8?
        "8",                   # What is 24 divided by 3?
        "24",                  # What is the sum of 14 and 10?
        "12",                  # What is 19 minus 7?
        "25",                  # What is 5 times 5?
        "5",                   # What is 30 divided by 6?
        "22",                  # What is 13 + 9?
        "17",                  # What is the difference between 21 and 4?
        "14",                  # What is 2 times 7?
        "2",                   # What is 18 divided by 9?
        "8",                   # What is 16 - 8?
        "16",                  # What is 10 + 6?
        "24",                  # What is the product of 3 and 8?
        "9",                   # What is 27 divided by 3?
        "21",                  # What is the sum of 15 and 6?
        "11",                  # What is 22 minus 11?
        "20",                  # What is 5 times 4?
        "4",                   # What is 20 divided by 5?
        "24",                  # What is 17 + 7?
        "15",                  # What is the difference between 30 and 15?
        "20",                  # What is 4 times 5?
        "4",                   # What is 28 divided by 7?
        "12",                  # What is 18 - 6?
        "21",                  # What is 10 + 11?
        "12",                  # If a hexagon has a side length of 2, what is its perimeter?
        "27",                  # What is 9 times 3?
        "4",                   # What is 24 divided by 6?
        "19",                  # What is 14 + 5?
        "18",                  # What is the difference between 27 and 9?
        "14",                  # What is 7 times 2?
        "7",                   # What is 21 divided by 3?
        "6",                   # What is 12 - 6?
        "21",                  # What is 13 + 8?
        "18",                  # What is the product of 6 and 3?
        "6",                   # What is 30 divided by 5?
        "23",                  # What is the sum of 16 and 7?
        "8",                   # What is 20 minus 12?
        "18",                  # What is 2 times 9?
        "9",                   # What is 18 divided by 2?
        "10",                  # What is 15 - 5?
        "14",                  # What is 6 + 8?
        "28",                  # What is the product of 7 and 4?
        "7",                   # What is 35 divided by 5?
        "22",                  # What is the sum of 12 and 10?
        "20",                  # What is 25 minus 5?
        "40",                  # What is 8 times 5?
        "5",                   # What is 40 divided by 8?
        "25"                   # What is 50 minus 25?
    ]
}