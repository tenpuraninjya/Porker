def open_hands(list):
    cnt = ""
    mark = [list[0][0],list[1][0],list[2][0]]
    nums = [list[0][1],list[1][1],list[2][1]]
    nums.sort()
    #print(f"コンビネーションファイルの{mark}です")
    #print(f"コンビネーションファイルの{nums}です")

# ストレート
    if nums[0] == (nums[1]-1) and nums[0] == (nums[2]-2):
        cnt += "ストレート" 
        #cnt += 6 
# フラッシュ
    if mark[0] == mark[1] and mark[1] == mark[2]:
        cnt = "フラッシュ"
        #cnt += 5    
# スリーカード
    if nums[0] == nums[1] and nums[1] == nums[2]:
        cnt += "スリーカード"
        #cnt += 3
# ワンペア
    if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
        cnt += "ワンペア"
        #cnt += 1
    else:
        cnt += "ブタ"
        #cnt += 0    
    return cnt