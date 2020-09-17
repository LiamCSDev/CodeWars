# First letter must be a hashtag
# All word must have their first letter capitalized
# If the final result is longer than 140 chars it must return false
# If the input is empty, return false
def generate_hashtag(s):
    if (len(s) > 140 or len(s) == 0): 
        return False
    else:
        return '#' + s.title().replace(" ", "")

print(generate_hashtag('')==False)
print(generate_hashtag('Codewars')=='#Codewars')
print(generate_hashtag('Codewars      ')=='#Codewars')
print(generate_hashtag('Codewars Is Nice')=='#CodewarsIsNice')
print(generate_hashtag('codewars is nice')=='#CodewarsIsNice')
print(generate_hashtag('CodeWars is nice')=='#CodewarsIsNice')
print(generate_hashtag('c i n')=='#CIN')
print(generate_hashtag('codewars  is  nice') =='#CodewarsIsNice')
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False)
