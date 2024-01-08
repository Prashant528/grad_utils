#### Why not for onboarding process?
- Onboarding task is a one time task and if the documents are proper and well-organized(e.g. flosscoach) then the task can be done once and the developers don't need to remember most of the things during the actual contribution process.
- People usually want to get through the onboarding process as quickly as possible and get started with the contribution. (I think it's a valid assumption since people are there to contribute, not to learn the contribution process in detail.)

#### Why for project (contribution or design) history?
- ##### From this paper:[[Learning from Project History]]
	- But newcomers/contributors need the access to collective ==project memory== of the project to be able to make changes, especially when mentoring is not available easily to teach them  the structure of the project, coding standards, common programming patterns, tools, and work practices in general. 
	- What is project memory? 
		- Project memory = Mailing lists + VCS + Issue trackers + project documents.
		- Developers need to keep coming back to this information for contributing.
- ##### From Brad's paper [[RESEARCH/Brad's papers/Hard-to-Answer Questions about Code|Hard-to-Answer Questions about Code]]
	- Newcomers as well as developers need to know the evolution of the project (feature-wise or code-wise)
	- For example, some frequently asked questions from developers (during the development process) are about the history of the code: ![[Pasted image 20240106121023.png]]
- ##### From this paper [[Architecture and Design Intent in Component & COTS Based Systems]]
	- We spend as much as 80% of our time in discovery or rediscovery in legacy systems. Much of this time is spent trying to determine the original intent of the architecture, design and code.

### How to get the information about project history?
- The resources to get that information are project documents, git commit logs or change logs(mostly generated automatically from commits and PRs).
- Change logs are just bullet points, give short information about the changes.
- However, there are different formats of change logs too. Examples of change logs:
	- https://github.com/casey/just/blob/master/CHANGELOG.md
	- https://github.com/audacity/audacity/blob/master/CHANGELOG.txt
	- Change logs like the first one can give us the intent of the changes (from linked PRs).
	- Some (like the second one) also lack the information about the developer, commits that were made to develop/debug the actual feature/bug they wanted to solve.  {We may need to add extra processing steps to get this information.}
- Stories could help to merge this information together to make the logs more informative.

### Our bet: Stories are memorable than just bullet points.
- Obviously, stories will have more words and text to go through than just bullet points.
- The initial burden increases. But once the developers go through the story, we are hoping that more information about the project history is committed to their memory and they would feel more comfortable with the project and to make any changes.
- Evidences that stories increase recall:
	- There are mixed results from experiments but from all of the experiments (till 2021), stories are better recalled and understood. [[Memory and comprehension of narrative versus expository texts (A meta-analysis)]]
	-  Example can be found here even though the paper gives mixed results: [[Processing and memory of information presented in narrative or expository texts]]
	- Stories can increase recall of a list of words by 6-7 times. [[Narrative stories as mediators for serial learning]]
	- Stories are about **12 times as memorable** as statistics.[[RESEARCH/Processing texts vs narratives/Made to stick|Made to stick]]

#### Challenges:
1.  We don't really have a good story format.
	- Looking at the common design features of [[Hybrid texts]].
	- Looking at ways of creating memorable stories. [[RESEARCH/Processing texts vs narratives/Made to stick|Made to stick]]
	- Main target should be creating a story which is both ==interesting and informative.==  [[Strategies for increasing text-based interest and students' recall of expository texts]]
	- The interesting part is difficult to create for software development process.

