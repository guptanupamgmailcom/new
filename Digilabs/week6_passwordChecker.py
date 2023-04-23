import re

def password_strength(password):
    # Calculate the password length score
    length_score = min(2 * len(password), 20)

    # Calculate the password complexity score
    complexity_score = 0
    if re.search("[a-z]", password):
        complexity_score += 1
    if re.search("[A-Z]", password):
        complexity_score += 1
    if re.search("[0-9]", password):
        complexity_score += 1
    if re.search("[^a-zA-Z0-9]", password):
        complexity_score += 1
    complexity_score = min(max(complexity_score, 2), 4) * 10

    # Calculate the password entropy score
    entropy_score = min(10, int(len(password) / 4))

    # Calculate the password overall strength score
    strength_score = length_score + complexity_score + entropy_score

    # Calculate the password strength percentage
    strength_percentage = int((strength_score / 70) * 100)

    # Return the password strength percentage and recommendations
    recommendations = []
    if length_score < 10:
        recommendations.append("Use a longer password.")
    if complexity_score < 30:
        recommendations.append("Use a more complex password with a mix of lowercase letters, uppercase letters, digits, and special characters.")
    if entropy_score < 3:
        recommendations.append("Use a more random password.")
    return strength_percentage, recommendations

# Ask the user for a password input
password = input("Enter your password: ")

# Call the password_strength function to get the password strength percentage and recommendations
strength_percentage, recommendations = password_strength(password)

# Print the password strength percentage and recommendations
print("Password strength:", strength_percentage, "%")
if recommendations:
    print("Recommendations:")
    for recommendation in recommendations:
        print("-", recommendation)