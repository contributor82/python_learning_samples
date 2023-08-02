from urllib.request import urlopen

try: 

    with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
        print('I am here')
        for line in response:
            line = line.decode()             # Convert bytes to a str
            if line.startswith('datetime'):
                print(line.rstrip()) 

except:
    print('Exception occurred : No internet access. ')
    