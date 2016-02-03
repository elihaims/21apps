import argparse

from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

def get_text(img_url, server_ip=None):

	if server_ip == None:
		server_url = "http://10.244.64.235:5003/"
	else:
		server_url = "http://"+server_ip+"/"
	sel_url = server_url+"analyze?img_url={0}"
	response = requests.get(url=sel_url.format(img_url))
	print("Text found in your image: ")
	print(response.text)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Get text within image")
	parser.add_argument('-u', help="url of image on which to perform optical character recognition")
	parser.add_argument('--ip', help="ip and port of BC hosting sentiment server (e.g. --ip 10.244.64.235:5003)")
	args = parser.parse_args()

	if args.u == None:
		print("Must specify image URL")
		exit()

	if args.ip != None:
		if len(args.ip.split('.')) != 4 or len(args.ip.split(':')) != 2:
			print("Incorrectly formated ip (e.g. 10.244.64.235:5003)")
			exit()

	get_text(args.u, args.ip)