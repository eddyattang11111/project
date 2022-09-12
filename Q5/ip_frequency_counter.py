import re 

def count_ip(filename):
    all_ip = {}
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            current = line.strip()
            pattern = re.search("([0-9]{1,3}[\.]){3}[0-9]{1,3}",current)
            ip = pattern.group(0)

            if str(ip) not in all_ip:
                all_ip[str(ip)]=0
            all_ip[str(ip)]+=1

    for k,v in all_ip.items():
        print("{0}\t{1}".format(v,k))

if __name__ == "__main__":

    filename = "<full path of log file>"

    count_ip(filename)

