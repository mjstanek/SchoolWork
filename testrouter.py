import subprocess

rawoutput = subprocess.run(["ip", "route"], capture_output=True)
subprocessresult = rawoutput.stdout.decode()
# print(type(subprocessresult))

for i in subprocessresult.split('\n'):
    if i.startswith('default via'):
        routerip = i.split(' ')[2]
        print(routerip)
        # print('-------------')