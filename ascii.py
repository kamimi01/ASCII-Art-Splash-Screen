import random
import os

# txtファイルを格納しているGitレポジトリのディレクトリ
gitRepositoryDir = "https://raw.githubusercontent.com/kamimi01/ASCII-Art-Splash-Screen/master/art/"
numOfFiles = 1
txtExtention = ".txt"

# ランダムにファイルを取得する
i = random.randrange(numOfFiles) + 1 
website = gitRepositoryDir + str(i) + txtExtention

# curlコマンド実行
os.system("curl " +  website)
