def levenshtein_similarity(s1, s2):
    # Calculate the Levenshtein distance
    distance = levenshtein_distance(s1, s2)
    
    # Calculate the maximum length between the two strings
    max_length = max(len(s1), len(s2))
    
    # Calculate the similarity by subtracting the normalized distance from 1
    similarity = 1 - (distance / max_length)
    
    return similarity

def levenshtein_distance(s1, s2):
    # Initialize a matrix of zeros with dimensions (len(s1) + 1) x (len(s2) + 1)
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    # Fill in the first row and column of the matrix
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j
    
    # Calculate the minimum number of edits required to transform s1 into s2
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,         # Deletion
                               matrix[i][j - 1] + 1,         # Insertion
                               matrix[i - 1][j - 1] + substitution_cost)  # Substitution
    
    # Return the value in the bottom-right cell of the matrix (Levenshtein distance)
    return matrix[len(s1)][len(s2)]

class chatbot():
    qna = [str,str]

    def __init__(self):
        pass

    def chat(self, text):
        return text
    