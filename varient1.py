def main():
  # 12x12の表を作成
  table = [[0 for i in range(12)] for j in range(12)]

  # 表に1から144までの数字を代入
  for i in range(12):
    for j in range(12):
      table[i][j] = (i+1) * (j+1)

  # 表を出力
  for row in table:
    print(" ".join(map(str, row)))

if __name__ == "__main__":
  main()

"""
chatGPTに以下プロンプトをなげて出力されたものを修正して完成しました。
12x12 の表形式 python 形式で出力すると

"""
