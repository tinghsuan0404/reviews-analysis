#讀檔案
data = []
count = 0
with open('original.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:# %=求餘數
		    print(len(data))

print('檔案讀取完畢', '總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均留言長度', sum_len/len(data))

#篩選出長度小於100的留言
new = []
for d in data:#一次讀一筆
    if len(d) < 100:
    	new.append(d)
print("一共有", len(new), "筆留言長度小於100")
#讀取第一筆資料
print(new[0])