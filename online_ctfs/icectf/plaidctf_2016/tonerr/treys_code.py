#!/usr/bin/env python

from Crypto.Random import random, atfork
from Crypto.Hash import SHA256

import SocketServer,threading,os,time

msg = """Welcome to the Tonnerre Authentication System!\n"""
flag = "REDACTED"

N = 168875487862812718103814022843977235420637243601057780595044400667893046269140421123766817420546087076238158376401194506102667350322281734359552897112157094231977097740554793824701009850244904160300597684567190792283984299743604213533036681794114720417437224509607536413793425411636411563321303444740798477587L
g = 9797766621314684873895700802803279209044463565243731922466831101232640732633100491228823617617764419367505179450247842283955649007454149170085442756585554871624752266571753841250508572690789992495054848L
v = 'ebedd14b5bf7d5fd88eebb057af43803b6f88e42f7ce2a4445fdbbe69a9ad7e7a76b7df4a4e79cefd61ea0c4f426c0261acf5becb5f79cdf916d684667b6b0940b4ac2f885590648fbf2d107707acb38382a95bea9a89fb943a5c1ef6e6d064084f8225eb323f668e2c3174ab7b1dbfce831507b33e413b56a41528b1c850e59'
# salt = 'd14058efb3f49bd1f1c68de447393855e004103d432fa61849f0e5262d0d9e8663c0dfcb877d40ea6de6b78efd064bdd02f6555a90d92a8a5c76b28b9a785fd861348af8a7014f4497a5de5d0d703a24ff9ec9b5c1ff8051e3825a0fc8a433296d31cf0bd5d21b09c8cd7e658f2272744b4d2fb63d4bccff8f921932a2e81813'
# This should import the fields from the data into the dictionary.
# the dictionary is indexed by username, and the data it contains are tuples
# of (salt, verifier) as numbers. note that the database stores these in hex.

permitted_users = {'get_flag': (0xd14058efb3f49bd1f1c68de447393855e004103d432fa61849f0e5262d0d9e8663c0dfcb877d40ea6de6b78efd064bdd02f6555a90d92a8a5c76b28b9a785fd861348af8a7014f4497a5de5d0d703a24ff9ec9b5c1ff8051e3825a0fc8a433296d31cf0bd5d21b09c8cd7e658f2272744b4d2fb63d4bccff8f921932a2e81813, 0xebedd14b5bf7d5fd88eebb057af43803b6f88e42f7ce2a4445fdbbe69a9ad7e7a76b7df4a4e79cefd61ea0c4f426c0261acf5becb5f79cdf916d684667b6b0940b4ac2f885590648fbf2d107707acb38382a95bea9a89fb943a5c1ef6e6d064084f8225eb323f668e2c3174ab7b1dbfce831507b33e413b56a41528b1c850e59)}

def H(P):
  h = SHA256.new()
  h.update(P)
  return h.hexdigest()


def tostr(A):
  return hex(A)[2:].strip('L')

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def handle():

  username = "get_flag"


  # public_client = int(req.recv(512).strip('\n'), 16) % N
  public_client = egcd(int(v,16), N)[1] + N

  random_server = random.randint(2, N-3)
  public_server = pow(g, random_server, N)
  residue = (public_server + permitted_users[username][1]) % N
  print(tostr(permitted_users[username][0]) + '\n')
  print(tostr(residue) + '\n')

  session_secret = (public_client * permitted_users[username][1]) % N
  session_secret = pow(session_secret, random_server, N)
  session_key = H(tostr(session_secret))

  # proof = req.recv(512).strip('\n')
  proof = H(tostr(residue) + H(tostr(1)))


  if (proof != H(tostr(residue) + session_key)):
    print('Sorry, not permitted.\n')
    req.close()
    return

  our_verifier = H(tostr(public_client) + session_key)
  print our_verifier + '\n'

  print ('Congratulations! The flag is ' + flag + '\n')


handle()