import os
import sys
import json
import hashlib
from shlex import split
from getpass import getpass
import client as pcl
try:
	import readline
except ImportError:
	readline = None

class LoginError(Exception):
	def __init__(self, message=""):
		super(LoginError, self).__init__(message)

def get_json(filename):
	filename = os.path.join(os.path.dirname(__file__), "json", filename + ".json")
	try:
		with open(filename) as file:
			return json.load(file)
	except (IOError, ValueError):
		return {}

def set_json(filename, data):
	filename = os.path.join(os.path.dirname(__file__), "json", filename + ".json")
	try:
		with open(filename, "w") as file:
			json.dump(data, file)
	except IOError:
		return False
	return True

# TODO
def get_remember():
	if "-r" in sys.argv:
		index = sys.argv.index("-r")
		remember = sys.argv.pop(index + 1)
		sys.argv.pop(index)
		if remember == "yes":
			return True
		if remember == "no":
			return False
		if remember == "ask":
			return None
		raise LoginError('Unknown remember option: "{}"'.format(remember))
	return None

def complete(options):
	def inner_complete(text, state):
		line = readline.get_line_buffer()
		return [option for option in options if option.startswith(line)][state]
	return inner_complete

def get_input(prompt=None, options=None):
	if readline is not None and options is not None:
		completer_delims = readline.get_completer_delims()
		completer = readline.get_completer()

		readline.set_completer_delims("")
		readline.parse_and_bind("tab: complete")
		readline.set_completer(complete(options))
	try:
		return raw_input() if prompt is None else raw_input(prompt)
	finally:
		if readline is not None and options is not None:
			readline.set_completer_delims(completer_delims)
			readline.set_completer(completer)

def get_cpps(servers, cpps=None):
	if cpps is None:
		cpps = get_input("CPPS: ", servers.keys())
	cpps = cpps.lower()
	if cpps not in servers:
		raise LoginError('CPPS "{}" not found'.format(cpps))
	return cpps

def get_user(penguins, cpps, user=None):
	if user is None:
		user = get_input("Username: ", penguins.get(cpps, {}).keys())
	return user.lower()

def get_password(penguins, cpps, user, remember=None):
	if cpps in penguins and user in penguins[cpps]:
		return penguins[cpps][user], True
	password = getpass("Password: ")
	if remember is None:
		remember = get_input("Remember? [y/N] ", ["y", "N"]) == "y"
	if remember:
		if cpps not in penguins:
			penguins[cpps] = {}
		penguins[cpps][user] = hashlib.md5(password).hexdigest()
		set_json("penguins", penguins)
	return password, False

def get_server(servers, cpps, server=None):
	if server is None:
		server = get_input("Server: ", servers[cpps]["servers"].keys())
	server = server.lower()
	if server not in servers[cpps]["servers"]:
		raise LoginError('Server "{}" not found'.format(server))
	return server

def get_client(servers, cpps, server, logger=None):
	if "ip" in servers[cpps]:
		login_ip = game_ip = servers[cpps]["ip"]
		login_port = servers[cpps]["login"]
		game_port = servers[cpps]["servers"][server]
	else:
		login_ip, login_port = servers[cpps]["login"].split(":")
		login_port = int(login_port)
		game_ip, game_port = servers[cpps]["servers"][server].split(":")
		game_port = int(game_port)
	magic = servers[cpps].get("magic")
	single_quotes = servers[cpps].get("single_quotes")
	return pcl.Client(login_ip, login_port, game_ip, game_port, magic, single_quotes, logger)

def get_penguin(cpps=None, server=None, user=None, remember=None, client=None):
	servers = get_json("servers")
	penguins = get_json("penguins")
	try:
		cpps = get_cpps(servers, cpps)
		user = get_user(penguins, cpps, user)
		password, encrypted = get_password(penguins, cpps, user, remember)
		server = get_server(servers, cpps, server)
	except (KeyboardInterrupt, EOFError):
		raise LoginError()
	return cpps, server, user, password, encrypted, get_client(servers, cpps, server) if client is None else client

def remove_penguin(cpps, user, penguins=None, ask=True):
	if penguins is None:
		penguins = get_json("penguins")
	if cpps in penguins and user in penguins[cpps] and (not ask or get_input("Remove penguin? [y/N] ", ["y", "N"]) == "y"):
		print "Removing {}...".format(user)
		del penguins[cpps][user]
		set_json("penguins", penguins)

def read_command(commands):
	while True:
		try:
			command = split(get_input(">>> ", commands.keys()))
		except ValueError as e:
			print e.message
			continue
		except KeyboardInterrupt:
			print
			continue
		if not command:
			continue
		command, params = command[0], command[1:]
		if command not in commands:
			print 'Command "{}" does not exist'.format(command)
			continue
		break
	return commands[command], command, params

def execute_command(client, function, command, params):
	try:
		message = function(client, *params)
	except TypeError as e:
		if function.__name__ + "() takes" not in e.message:
			raise
		print 'Command "{}" does not take {} arguments'.format(command, len(params))
	except KeyboardInterrupt:
		print
	except LoginError as e:
		print e.message
	except pcl.ClientError:
		pass
	else:
		if function not in vars(pcl.Client) and message is not None:
			print message
