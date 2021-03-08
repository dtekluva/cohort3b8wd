Friends = int(input( "Enter (1) if you know the names of the friends,\nEnter (2) if you want to list them : "))
if Friends == 1: 
    bolas_sweet =int(input("How many sweets does Bola have : "))
    Tola_sweet =int(input("How many sweets does Tola have : "))
    Obum_sweet =int(input("How many sweets does sum have : "))

    All_sweets = bolas_sweet+Tola_sweet+Obum_sweet

    all_friends = [bolas_sweet,Tola_sweet,Obum_sweet]
    count_friends = len(all_friends)
    share = All_sweets / count_friends

    split_share = All_sweets // count_friends
    remainder = All_sweets % count_friends

    # if isinstance(share, float):
    if remainder > 0:
        print (f"Each friend will get {split_share} sweets with the remaining {remainder}sweets thrown away" )
        print (f"because all friends had {All_sweets}sweets in all ")
    else:
        print (f"Each friend will get {split_share} sweets" )
        print (f"because all friends had {All_sweets}sweets in all ")

elif Friends == 2:
    List_friends = input("Enter list of friend seperated by comma : ")
    Total_sweets = int(input(" Howmay sweets in all do they have : "))
    count = len(List_friends.split(","))
    equal_share = Total_sweets // count
    remainder_2 = Total_sweets % count

    if remainder_2 > 0:
        print (f"Each friend will get {equal_share} sweets with the remaining {remainder_2}sweets thrown away" )
        print (f"because the {count} friends had {Total_sweets}sweets in all ")
    else:
        print (f"Each friend will get {equal_share} sweets" )
        print (f"because the {count} friend(s )had {Total_sweets}sweets in all ")

# values =("Enter values for (a) and (b)")
# print( values)
# a = int(input ("a = "))
# b = int(input ("b = "))
# bool1= a>b
# bool2= b>a
# print( f"{a} is greater than {b}: {bool1}")
# print( f"{b} is greater than {a}: {bool2}")

# text = " Hello world"[::-1]
# print(text)

# x=5
# a= 1+x
# print (a)
