import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Please provide the input file!")
        sys.exit(1)
    filein  = sys.argv[1]

    with open(filein, "r") as f:
        for i in f:
            r = requests.get(i)
            if r.status_code == 200:
                print (i)

if __name__ == '__main__':
    main()
