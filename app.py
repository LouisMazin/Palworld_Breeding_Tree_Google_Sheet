import Graph,sys

parent = sys.argv[1]
child = sys.argv[2]
number = sys.argv[3]
def main():
    return Graph.getJSONShortestWays(parent, child,int(number))

if __name__ == '__main__':
    main()