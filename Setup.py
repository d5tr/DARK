import os

XX = os.getcwd()
CLAN = str(XX)
cc =CLAN.replace('DARK', '')

os.system('chmod +x DARK.sh')
os.system(f'cd {cc} && cp -r DARK /root')
os.system('mv DARK.sh /bin/DARK')

print('Done ... ')