print("Enter runs scored by each player in 60 balls: ")
player_1 = int(input("player 1 : "))
player_2 = int(input("player 2 : "))
player_3 = int(input("player 3 : "))

print("\n strike rate index - ")
print("player 1 -",(player_1/60)*100)
print("player 2 -",(player_2/60)*100)
print("player 3 -",(player_3/60)*100)

print("\n runs scored if players played 60 more balls : ")
print("player 1 -",player_1*2)
print("player 2 -",player_2*2)
print("player 3 -",player_3*2)

print("\n maximum number of sixes each player could have hit : ")
print("player 1 -",player_1//6)
print("player 2 -",player_2//6)
print("player 3 -",player_3//6)
