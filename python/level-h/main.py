def voteSystem(n, votes, project_range):
    if project_range == 0:
		return 'No projects, Sorry !'
	projects={};
	for i in range(0,n):
		vote = votes[i]
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
