import random
import os

# txtファイルを格納しているGitレポジトリのディレクトリ
gitRepositoryDir = "https://raw.githubusercontent.com/kamimi01/ASCII-Art-Splash-Screen/master/art/"

# ファイル数をカウント
path = "./art"
files = os.listdir(path)
numOfFiles = len(files)

# ランダムにファイルを取得する
i = random.randrange(numOfFiles) + 1 
website = gitRepositoryDir + str(i) + ".txt"

# curlコマンド実行
os.system("curl " +  website)
