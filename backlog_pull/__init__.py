import backlog_puller
import sys


def main(argv):
    if len(argv) == 2:
        request = backlog_puller.GamesRequest(argv[1])
        parser = backlog_puller.BacklogHTMLParser()
        parser.feed(request.get_raw_page())
        print parser.backlog
    else:
        print("Incorrect number of arguments. Please pass just your username and try again")

if __name__ == 'main':
    main(sys.argv)