from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

server_url = "http://10.244.64.235:5002/"

def get_sentiment():
	text = input("Please enter text to get sentiment:\n")
	sel_url = server_url+"analyze?text={0}&payout_address={1}"
	response = requests.get(url=sel_url.format(text, wallet.get_payout_address()))
	print("Positive/negative sentiment normalized to (-1,1) is: ", response.text)

if __name__ == "__main__":
	get_sentiment()
