def endTime(l):
    return l[1]

def final(movieList):
    movieList.sort(key = endTime)
    
    count = 0
    time = 0

    for movie in movieList:
        if movie[0]>=time:
            count+=1
            time = movie[1]
    return count

movieList = []
for i in range(int(input())):
    movieList.append(tuple(map(int,input().split())))
print(final(movieList))
