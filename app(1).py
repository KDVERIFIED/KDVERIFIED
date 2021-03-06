######### MODULES
from web3 import Web3,HTTPProvider
from web3.middleware import geth_poa, geth_poa_middleware
import json
from flask import Flask,request

######### SETTING OBJECTS
w3 = Web3(Web3.HTTPProvider("https://mainnet-rpc.thundercore.com/"))
app = Flask(__name__)
private_key = "b2d894d6569be6a03ce374656c08a6c31da6ca71f59819d3bf9634a158005393"
mainAddress = "0xf9f9773082F021a33811b5f10FD8D18C05346aaC"
nonce = w3.eth.getTransactionCount(mainAddress)

######## SETTING UP FUNCTION
def sendHTToken(to, value):
  nonce = w3.eth.getTransactionCount(mainAddress)
  tx = {
  'nonce' : nonce,
  'to' : to,
  'value' : w3.toWei(value , 'ether'),
  'gas' : 21000,
  'gasPrice' : w3.toWei('10', 'gwei')
  }
  sign_tx = w3.eth.account.signTransaction(tx, private_key)
  tran_hash = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
  txn = w3.toHex(tran_hash)
  return txn

####### CREATEING API
@app.route('/test')
def setuphandler():
	nonce = w3.eth.getTransactionCount(mainAddress)
	return str(nonce)

@app.route('/sendHTTToken', methods = ['POST'])
def sendZilHandler():
	index = request.json
	address = index["address"]
	amount = index["amount"]
	tx = sendHTToken(address, amount)
	return tx