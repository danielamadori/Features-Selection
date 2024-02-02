def featureScoreMessage(scoreFeatures):
    message = 'Score: '
    for metric in scoreFeatures:
        message += f'{metric}: {scoreFeatures[metric]:.6f}, '

    # Return the message without the last comma and space
    return message[:-2]

def printScore(selected_features, selected_features_score):
    print("Selected features: ")
    for i in range(len(selected_features)):
        print('\t-Feature: {}, {}'.format(selected_features[i], featureScoreMessage(selected_features_score[i])))
    print("--------------------------------------------------")
def printRemainingFeatures(remaining_features):
    print("Remaining features: ")
    for i in range(len(remaining_features)):
        print('\t-Feature: {}'.format(remaining_features[i]))
    print("--------------------------------------------------")

def printWorstScore(eliminated_features, eliminated_features_worst_score):
    print("Eliminated features: ")
    for i in range(len(eliminated_features)):
        print('\t-Feature: {}, {}'.format(eliminated_features[i], featureScoreMessage(eliminated_features_worst_score[i])))
    print("--------------------------------------------------")

def printScoreDetails(selected_features, selected_features_score, remaining_features):
    printScore(selected_features, selected_features_score)
    printRemainingFeatures(remaining_features)

def printWorstScoreDetails(remaining_features, eliminated_features, eliminated_features_worst_score):
    printWorstScore(eliminated_features, eliminated_features_worst_score)
    printRemainingFeatures(remaining_features)

def printFinalScore(selected_features, selected_features_score, eliminated_features, eliminated_features_worst_score):
    printScore(selected_features, selected_features_score)
    printWorstScore(eliminated_features, eliminated_features_worst_score)

def printFinalScoreDetails(selected_features, selected_features_score, remaining_features, eliminated_features, eliminated_features_worst_score):
    printScore(selected_features, selected_features_score)
    printWorstScore(eliminated_features, eliminated_features_worst_score)
    printRemainingFeatures(remaining_features)