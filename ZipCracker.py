__AUTHOR__ = 'Vondri'
__VERSION__ = '1.0.0'
__GITHUB__ = 'https://github.com/Vondri'

from zipfile import BadZipFile, ZipFile
import argparse
import os
import sys

try:
    import pyzipper
except ModuleNotFoundError:
    os.system('pip install pyzipper')

if sys.platform.startswith('win'): 
    os.system('cls') 
else: 
    os.system('clear')

parser = argparse.ArgumentParser(description='The python script is written to crack the password of a zip file')
parser.add_argument('-z','--zip', help='Zip file to crack.', required=True)
parser.add_argument('-w', '--wordlist', help='Wordlist', required=True)
parser.add_argument('-s', '--silent', help='Run script without banner', required=False, action="store_true")
args = parser.parse_args()

if not args.silent:
    print(f'''
  \033[1m\033[38;5;21m███████╗██╗██████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
  \033[1m\033[38;5;27m╚══███╔╝██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  \033[1m\033[38;5;33m  ███╔╝ ██║██████╔╝██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
  \033[1m\033[38;5;39m ███╔╝  ██║██╔═══╝ ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
  \033[1m\033[38;5;45m███████╗██║██║     ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
  \033[1m\033[38;5;51m╚══════╝╚═╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mAuthor:{__AUTHOR__} \033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mVersion: {__VERSION__}\033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mGithub: {__GITHUB__}\033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m''')

try:
    file = open(args.wordlist)
except FileNotFoundError:
    print('\033[1m\033[38;5;9mWordlist was not found.')
    sys.exit(0)
wordlist = file.readlines()

zipPath = os.path.abspath(args.zip)
wordlistPath = os.path.abspath(args.wordlist)

files = []
try:
    with pyzipper.AESZipFile(args.zip) as zip:
        files = zip.namelist()
except FileNotFoundError:
    print('\033[1m\033[38;5;9mZip was not found.\033[0m')
    sys.exit(0)


print(f'\033[38;5;245mFiles:\033[0m', end=' ')
for file in files:
    print(file, end=' ')
print(f'\n\033[38;5;245mZip:\033[0m {zipPath}')
print(f'\033[38;5;245mWordlist:\033[0m {wordlistPath}')
print(f'\033[38;5;245m=\033[0m'*50)
for i, word in enumerate(wordlist):
    try:
        with pyzipper.AESZipFile(args.zip) as zip:
            try:
                word = word.strip()
                password = word.strip().encode('utf-8')
                zip.setpassword(password)
                if(zip.read(zip.namelist()[-1])): 
                    print(f'\033[38;5;10m{i}/{len(wordlist)} -> {word} [+]\033[0m')
                    print(f'\033[38;5;245m=\033[0m'*50)
                    print(f'\033[38;5;2mPassword \033[4m\033[38;5;10m{word}\033[0m \033[38;5;2mon approach \033[4m\033[38;5;10m{i}\033[0m')
                    sys.exit(0)
            except RuntimeError:
                print(f'\033[38;5;9m{i}/{len(wordlist)} -> {word} [-]\033[0m')
    except FileNotFoundError:
        print('\033[1m\033[38;5;9mZip was not found.\033[0m')
        sys.exit(0)
print(f'\033[38;5;245m=\033[0m'*50)
print('\033[1m\033[38;5;9mPassword was not found\033[0m')

