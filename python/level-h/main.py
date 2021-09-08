def compute_executable_projects(n, participants_votes, project_range):
	if project_range == 0:
		return 'No projects, sorry!'
	projects={}
	for i in range(0,n):
		vote = participants_votes[i]
		for j in range(0,len(vote)):
			if j in projects:
				projects[j] = projects[j] + vote[j]
			else:
				projects[j] = vote[j]
	orderedProjects = {k: v for k, v in sorted(projects.items(), key=lambda item: item[1], reverse = True)}
	orderedProjectsKeys = [*orderedProjects.keys()]
	output =[]
	for i in range(0,project_range):
		output.append(orderedProjectsKeys[i] + 1)
	return output