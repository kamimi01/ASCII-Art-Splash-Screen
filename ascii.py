import random
import os
import settings

# txtファイルを格納しているローカルのディレクトリを取得
artFileDir = settings.artFileDir
txtExtention = ".txt"

# ディレクトリのファイル数を取得
files = os.listdir(artFileDir)
numOfFiles = len(files) - 1
print(numOfFiles)

# ランダムにファイルを取得する
i = random.randrange(numOfFiles) + 1
fileName = artFileDir + str(i) + txtExtention

# catコマンド実行
os.system("cat " + fileName)