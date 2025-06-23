import statistics

# Get 5 scores from the user
user_scores = []
for i in range(5):
    score = float(input(f"Enter score {i + 1}: "))
    user_scores.append(score)

# Calculate the mean
mean = statistics.mean(user_scores)
print(f"Mean of the scores: {mean:.2f}")

# Calculate the standard deviation
stdev = statistics.stdev(user_scores)
print(f"Standard Deviation of the scores: {stdev:.2f}")
