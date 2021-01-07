import random
import os
import settings

# txtファイルを格納しているローカルのディレクトリを取得
artFileDir = settings.artFileDir

# 使用可能なASCII Artのファイル拡張子
extList = [".txt", ".ascii"]

# ASCII Artとして出力するファイルを取得
files = os.listdir(artFileDir)
correctFiles = []

for file in os.listdir(artFileDir):
  base, ext = os.path.splitext(file)
  if ext in extList:
    correctFiles.append(file)

numOfFiles = len(correctFiles)

# ランダムにファイルを取得する
randomIndex = random.randrange(numOfFiles)
fileName = artFileDir + correctFiles[randomIndex]

# catコマンド実行
os.system("cat " + fileName)