import sys
import backlog_puller


def main():
    if len(sys.argv) == 2:
        request = backlog_puller.GamesRequest(sys.argv[1])
        parser = backlog_puller.BacklogHTMLParser()
        parser.feed(request.get_raw_page())
        print(parser.backlog)
    else:
        print("Incorrect number of arguments. Please pass just your username and try again")

if __name__ == 'main':
    main()
