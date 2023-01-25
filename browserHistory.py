class ListNode:
    def __init__(self, url="", prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node

    def back(self, steps: int) -> str:
        node = self.curr
        while (steps > 0 and node.prev):
            steps -= 1
            node = node.prev
        self.curr = node
        return self.curr.url
        

    def forward(self, steps: int) -> str:
        node = self.curr
        while (steps > 0 and node.next):
            steps -= 1
            node = node.next
        self.curr = node
        return self.curr.url
        
