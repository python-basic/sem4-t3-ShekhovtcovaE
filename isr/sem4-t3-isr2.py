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

    def print_out(self):
        print('Author: ', self.author)
        print('Post text: ', self.text)
    
class Comment(Post):
    """Комментарий"""
    def print_out(self):
        print('Author: ', self.author)
        print('Comment: ', self.text)
    
newPost = Post('bla-bla-bla', 'Vicky')
newComment = Comment('bla', 'Nicky')

newPost.print_out()
newComment.print_out()        
    
        