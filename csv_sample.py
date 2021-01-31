import datetime
import csv

# 日時の取得
now = datetime.datetime.now()
# ディレクトリの指定はここ
filename = './' + now.strftime('%Y%m%d_%H%M%S') + '.csv'

# # ファイル，1行目(カラム)の作成
# with open(filename, 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['x', 'y', 'z'])

x, y, z = 0, 0, 0
for _ in range(10):
    # なんらかの処理を書く
    x += 1
    y += 2
    z += 3
    # filenameを作成したファイル名に合わせる
    # writer.writerowでlistをcsvに書き込む
    with open(filename, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([x, y, z])
