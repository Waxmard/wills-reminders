import os

def main():
    message = "Hey Money, wanna bang?"
    recipient = "5715337817@txt.att.net"
    cmd = 'echo ' + message + ' | sendmail ' + recipient
    os.system(cmd)


if __name__ == "__main__":
    main()
