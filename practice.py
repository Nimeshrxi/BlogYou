class Post:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        
    def display(self):
        print(self.title)
        print(self.author)
        print(self.content)
        
obj = Post("Ikigai", "Graham Bell", "This is a book about finding purpose.")
obj1 = Post("Atomic Habits", "James Clear", "This book explains how small habits compound over time.")
obj2 = Post("Python Programming", "Nimesh", "Learning Python through building projects.")

posts = [obj, obj1, obj2]

for post in posts:
    post.display()
    print("-"*30)