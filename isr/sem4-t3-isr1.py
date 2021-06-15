class Post:
    """Запись в блоге"""
    def __init__(self, text = "", author = ""):
        self.__text = text
        self.__author = author
    @property
    def author(self):
        return self.__author

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        self.__text = new_text
    
class Comment(Post):
    """Комментарий"""
    
newPost = Post('bla-bla-bla', 'Vicky')
newComment = Comment('bla', 'Nicky')

print(newPost.author)
print(newPost.text)        

print(newComment.author)
print(newComment.text)         
    
        