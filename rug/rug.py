import sys
import getopt
from project import Project, RugError

def init(optdict={}, dir=None):
	return Project.init(dir, optdict.has_key('-b'))

def clone(optdict={}, url=None, dir=None, revset=None):
	if not url:
		raise RugError('url must be specified')

	return Project.clone(url, dir, revset, optdict.has_key('-b'))

def checkout(proj, optdict={}, rev=None):
	return proj.checkout(rev)

def fetch(proj, optdict={}, repos=None):
	return proj.fetch(repos)

def update(proj, optdict={}, repos=None):
	return proj.update(repos)

def status(proj, optdict={}):
	return proj.status()

def revset(proj, optdict={}, dst=None, src=None):
	if dst is None:
		return proj.revset()
	else:
		if src is None:
			return proj.revset_create(dst)
		else:
			return proj.revset_create(dst, src)

def add(proj, optdict={}, dir=None, name=None, remote=None):
	if not dir:
		raise RugError('unspecified directory')

	return proj.add(dir, name, remote)

def commit(proj, optdict={}, message=None):
	if not message:
		raise NotImplementedError('commit message editor not yet implemented') #TODO

	return proj.commit(message)

def publish(proj, optdict={}, remote=None):
	return proj.publish(remote)

def remote_list(proj, optdict={}):
	return proj.remote_list()

def remote_add(proj, optdict={}, remote=None, fetch=None):
	return proj.remote_add(remote, fetch)

#(function, pass project flag, options)
rug_commands = {
	'init': (init, False, 'b'),
	'clone': (clone, False, 'b'),
	'checkout': (checkout, True, ''),
	'fetch': (fetch, True, ''),
	'update': (update, True, ''),
	'status': (status, True, ''),
	'revset': (revset, True, ''),
	'add': (add, True, ''),
	'commit': (commit, True, ''),
	'publish': (publish, True, ''),
	'remote_list': (remote_list, True, ''),
	'remote_add': (remote_add, True, ''),
	#'reset': (Project.reset, True, ['soft', 'mixed', 'hard']),
	}

def main():
	if (len(sys.argv) < 2) or not rug_commands.has_key(sys.argv[1]):
		#TODO: write usage
		print 'rug usage'
	else:
		cmd = rug_commands[sys.argv[1]]
		[optlist, args] = getopt.gnu_getopt(sys.argv[2:], cmd[2])
		optdict = dict(optlist)
		if cmd[1]:
			ret = cmd[0](Project.find_project(), optdict, *args)
		else:
			ret = cmd[0](optdict, *args)

		if ret:
			print ret

if __name__ == '__main__':
	main()
