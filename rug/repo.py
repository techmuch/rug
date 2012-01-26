import project

class Repo(object):
	valid_repo = project.Project.valid_project

	def __init__(self, repo_dir):
		from project import Project
		self.project = Project(repo_dir)
		
		p = self.project
		mr = self.project.manifest_repo
		delegated_methods = {
			'valid_sha': mr.valid_sha,
			'valid_rev': mr.valid_rev,
			'update_ref': mr.update_ref,
			'head': mr.head,
			'rev_parse': mr.rev_parse,
			'symbolic_ref': mr.symbolic_ref,
			'is_descendant': mr.is_descendant,
			'can_fastforward': mr.can_fastforward,
			'remote_list': p.source_list,
			'remote_add': p.source_add,
			'remote_set_url': p.source_set_url,
			'remote_set_head': p.source_set_head,
			'branch': p.revset,
			'branch_create': p.revset_create,
			'status': p.status,
			'checkout': p.checkout,
			'commit': p.commit,
			'fetch': p.fetch,
			#'push': p.publish,
			#'test_push': p.test_publish,
			'merge': None, #TODO
			'dirty': None, #TODO
			'rebase': None, #TODO
		}

		self.__dict__.update(delegated_methods)

	@classmethod
	def init(cls, repo_dir=None):
		project.Project.init(project_dir=repo_dir)
		return cls(repo_dir)

	@classmethod
	def clone(cls, url, repo_dir=None, remote=None, rev=None):
		project.Project.clone(url, project_dir=repo_dir, remote=remote, revset=rev)
		return cls(repo_dir)

	def fetch(self, remote=None):
		#TODO: repo Project doesn't currently support fetching a particular source
		self.project.fetch()

	def add_ignore(self, pattern):
		raise NotImplemented('ignoring through rug repos not implemented')

	def push(self, remote, branch, force):
		#TODO: this is a hack to drop the branch and force args, because rug repos don't handle them. Fix
		return self.project.publish(remote)

	def test_push(self, remote, branch, force):
		#TODO: this is a hack to drop the branch and force args, because rug repos don't handle them. Fix
		return self.project.test_publish(remote)

project.Project.register_vcs('rug', Repo)
