score_board=[10,5,20,20,4,5,2,25,1]
highest_score=[]
lowest_score=[]
highest_score.append(score_board[0])
lowest_score.append(score_board[0])
score_board1=score_board[1:]
score_board2=score_board[1:]
final_list=[]
while(len(score_board1)!=0):
    if highest_score[len(highest_score)-1] > score_board1[0]:
        highest_score.append(highest_score[len(highest_score)-1])
    else:
        highest_score.append(score_board1[0])
    score_board1=score_board1[1:]

#print(highest_score)
#comparison
while(len(score_board2)!=0):
    if lowest_score[len(lowest_score)-1] < score_board2[0]:
        lowest_score.append(lowest_score[len(lowest_score)-1])
    else:
        lowest_score.append(score_board2[0])
    score_board2=score_board2[1:]
#print(lowest_score)
count1=0
count2=0
for i in range(0,len(highest_score)-1):
    if highest_score[i]<highest_score[i+1]:
        count1+=1
    else:
        continue
final_list.append(count1)
for i in range(0,len(lowest_score)-1):
    if lowest_score[i]>lowest_score[i+1]:
        count2=count2+1
    else:
        continue
final_list.append(count2)
print(final_list)
