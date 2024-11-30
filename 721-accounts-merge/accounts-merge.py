class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # create graph
        graph = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name
        
        
        # traverse the graph using DFS
        visited = set()
        merged_accounts = []
        def dfs(email, emails):
            emails.append(email)
            visited.add(email)
            for neighbour in graph[email]:
                if neighbour not in visited:
                    dfs(neighbour, emails)
                
        


        for email in graph:
            if email not in visited:
                emails = []
                dfs(email,emails)
                merged_accounts.append([email_to_name[email]]+sorted(emails))
        return merged_accounts
        