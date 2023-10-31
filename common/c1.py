class Article:
    author = ""
    title = ""
    content = ""
    likes = 0

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:15]
    
a1 = Article()
a1.author = "Amit"
a1.title = "Python is awesome"
a1.content = "Some content will be here soon"
a1.likes = "1000"

a2 = Article()
a2.author = " vansh"
a2.title = "js is awesome"
a2.content = "js is the awesome language"
a2.likes = " 1000101"


a3 = Article()
a3.author = "Aniket"
a3.title = "css"
a3.content = "best language for design"
a3.likes = " 41042"

print("Our articles are:")
print(a1)
print(a1.summary())
print(a2)
print(a2.summary())
print(a3)
print(a3.summary())