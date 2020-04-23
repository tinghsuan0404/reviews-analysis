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