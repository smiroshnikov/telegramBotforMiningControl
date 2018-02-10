import os
from os.path import join, getsize

for root, dirs, files in os.walk('H:\\\Development\\telegramBotforMiningControl\\simpleBlockChain'):
    # DEAR GOD , i JUST LOVE PYTHON !, THANK YOU !
    print(f"folder {root}\nhas following {'files' if len(files)>1 else 'file'} -> {files}")


# print("stuff" if False else 0)
# x = [1,2,3,4,5]
# print('files' if len(x)>1 else 'file')
