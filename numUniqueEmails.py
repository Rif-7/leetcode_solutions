class Solution:
    def numUniqueEmails(self, emails) -> int:
        unique = set()
        for e in emails:
            unique.add(self.getEmail(e))
        return len(unique)
    
    def getEmail(self, email):
        res = ""
        for i in range(len(email)):
            if email[i] == "@":
                return res + email[i:]
            elif email[i] == ".":
                continue
            elif email[i] == "+":
                while email[i] != "@":
                    i += 1
                return res + email[i:]
            res += email[i]
        return res