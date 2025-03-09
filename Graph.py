import random
words = [
    "run", "happy", "table", "she", "quickly", "dog", "play", "brave",
    "water", "kind", "they", "dance", "smart", "mountain", "strong",
    "he", "laugh", "sun", "beautiful", "read", "bright", "flower",
    "jump", "we", "quiet", "sky", "swim", "green", "explore", "it","on"
]

outputs=input().split()

arranged=[]

weights=[]

def balance(length):
    sum=0
    for i in range(len(length)):
        sum+=weights[i]
    print(sum)

balance(5)

