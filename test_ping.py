import ping
import sys


def usage():
    print("Usage: {0} [filename]".format(__file__))
    exit(1)


def ip_parse(filename):
    '''Parse the file to get the ip list, return the list'''
    with open(filename) as fp:
        ip_list = fp.readlines()
        return ip_list


def main():
    if len(sys.argv) < 2:
        usage()
    ip_list = ip_parse(sys.argv[1])
    print("{0:^20s}\t{1:^25s}\t{2:>5s}\t{3:>5s}\t{4:>5s}".format(
        "Tag", "IP", "Per", "Max", "Avg"))
    for line in ip_list:
        tag, ip = line.split()
        result = ping.quiet_ping(ip, count=10)
        print("{0:25s}\t{1:25s}\t{2:5d}%\t{3:5d}ms\t{4:5d}ms".format(
            tag, ip, result[0], int(result[1]), int(result[2])))


if __name__ == '__main__':
    main()
