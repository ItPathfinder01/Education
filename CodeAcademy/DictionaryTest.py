letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
 # Point 1
zipped = zip(letters, points)

letter_to_points = {letters: points for letters, points in zip(letters, points) }

# Point 2
letter_to_points[" "] = 0

# Point 3 - 8
def score_word(word):
  points_total = 0
  for letter in word:
    points_total += letter_to_points.get(letter, 0)
  return points_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH","EYES", "MACHINE"], "Lexi Con": ["ERASER","BELLY","HUSKY"], "Prof Reader": ["ZAP","COMA","PERIOD"] }

player_to_points = {}

for player, word in player_to_words.items():
   player_points = 0
   for word in word:
     player_points += score_word(word)
   player_to_points[player] = player_points
print(player_to_points)

