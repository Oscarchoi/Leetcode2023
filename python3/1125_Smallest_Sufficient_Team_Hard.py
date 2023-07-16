# 1125. Smallest Sufficient Team - Hard

class Solution:
    def __init__(self):
        self.dp = None
        self.res = []

    def smallestTeam(self, skills: List[int], index: int, required: int, current: [int], excluded: [int]):
        if index == len(skills):
            return

        if self.dp[index][required] > 0 and self.dp[index][required] <= len(current):
            return

        # without index
        self.smallestTeam(skills, index+1, required, current, excluded)

        # skip if it is excluded index
        if excluded[index]: return

        # with index
        current.append(index)

        mask = required & ~skills[index]
        if mask == 0:
            if len(self.res) == 0 or len(current) < len(self.res):
                self.res[:] = current[:]
        else:
            self.smallestTeam(skills, index+1, mask, current, excluded)

        if len(self.res) > 0:
            self.dp[index][required] = len(self.res)

        current.pop()
        return


    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        N = len(people)
        K = len(req_skills)

        req_skills_set = {skill: idx for idx, skill in enumerate(req_skills)}
        skills  = []
        for idx, person in enumerate(people):
            skill_set = 0
            for skill in person:
                skill_set |= 1 << req_skills_set[skill]
            skills.append(skill_set)

        excluded = [False] * N
        for i in range(N):
            for j in range(i+1, N):
                superset = skills[i] | skills[j]
                if superset == skills[i]:
                    excluded[j] = True
                elif superset == skills[j]:
                    excluded[i] = True

        total = (1 << len(req_skills)) - 1

        self.dp = [[-1] * (1<<K) for _ in range(N)]
        self.smallestTeam(skills, 0, total, [], excluded)
        return self.res