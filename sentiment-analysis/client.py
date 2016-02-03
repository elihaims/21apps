import argparse
import os.path

from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)


def get_sentiment(text=None, server_ip=None):
	if text == None:
		text = input("Please enter text to get sentiment:\n")
	if server_ip == None:
		server_url = "http://10.244.64.235:5002/"
	else:
		server_url = "http://"+server_ip+"/"
	sel_url = server_url+"analyze?text={0}"
	response = requests.get(url=sel_url.format(text))
	print("Positive/negative sentiment normalized to (-1,1) is: ", response.text)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Get social sentiment of text")
	parser.add_argument('-s', help="string to analyze (e.g. -s \"get sentiment of this text\")")
	parser.add_argument('-f', help="path to text file to analyze")
	parser.add_argument('--ip', help="ip and port of BC hosting sentiment server (e.g. --ip 10.244.64.235:5002)")
	args = parser.parse_args()
	if args.f != None:
		if os.path.isfile(args.f):
			with open(args.f) as f:
				text = f.read()
		else:
			print("File does not exist")
			exit()
	elif args.s != None:
		text = args.s
	else:
		text = None

	if args.ip != None:
		if len(args.ip.split('.')) != 4 or len(args.ip.split(':')) != 2:
			print("Incorrectly formated ip (e.g. 10.244.64.235:5002)")
			exit()

	get_sentiment(text, args.ip)