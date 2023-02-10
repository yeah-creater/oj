from Backend.models.solution.solution import Solution
from Backend.models.blog.blog import Blog
from Backend.models.file.file import File
from Backend.models.file.file import Comment
# 类型 以及 id
def find(t, id):
    try:
        id = int(id)
        if t == 'solution':
            solutions = Solution.objects.filter(id = id, show = True)
            if not solutions.exists():
               return 0
            return solutions[0].file.id
        elif t == 'blog':
            blogs = Blog.objects.filter(id = id, show = True)
            if not blogs.exists():
               return 0
            return blogs[0].file.id
        else:
            return 0
    except:
        return 0