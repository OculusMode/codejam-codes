# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
# NOT PERFECT YET, YOU CAN MAKE IT BETTER
def find_cost(str1,CJ,JC):
  size1 = len(str1)
  cost = 0
  for i in range(size1-1):
    mini_str = str1[i]+str1[i+1]
    if(mini_str)=="CJ":
      cost = cost + CJ
    elif(mini_str) == "JC":
      cost = cost + JC
  return cost

def pac(pattern, i=0, poss_combi = []):
    if i == len(pattern):
        poss_combi.append(''.join(pattern))
        return
#         return poss_combi
    # if the current character is `?`
    if pattern[i] == '?':
        for ch in "CJ":
            # replace `?` with 0 and 1
            pattern[i] = ch
            # recur for the remaining pattern
            pac(pattern, i + 1, poss_combi) 
            # backtrack
            pattern[i] = '?'
    else:
        # if the current character is 0 or 1, ignore it and
        # recur for the remaining pattern
        pac(pattern, i + 1, poss_combi)
    return poss_combi
    
T = int(input())
for _ in range(T):
    ip = input().split(' ')
    cjCost, jcCost, ccCost, jjCost = int(ip[0]), int(ip[1]), 0, 0
    string = ip[2]
#     print(string)
    combi = pac(list(string), i = 0, poss_combi = [])
#     print(combi)
    min_cost = 1000
    for idx in combi:
        final_cost = find_cost(idx, cjCost, jcCost)
#         print(final_cost)
        if final_cost < min_cost:
            #print(final_cost,min_cost)
            min_cost = final_cost
#             print(min_cost)
    print(f'Case #{_+1}: {min_cost}')
