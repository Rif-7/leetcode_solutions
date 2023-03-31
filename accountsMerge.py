class Solution:
    def accountsMerge(self, accounts):
        hashMap = {}  # name: [emails...]

        for acc in accounts:
            currEmail = set(acc[1:])
            new = [currEmail]
            for email in hashMap.get(acc[0], []):
                if currEmail.intersection(email):
                    currEmail.update(email)
                else:
                    new.append(email)
            hashMap[acc[0]] = new

        res = []
        for name, emails in hashMap.items():
            for e in emails:
                res.append([name] + sorted(list(e)))
        return res
