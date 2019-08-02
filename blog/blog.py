class Blog:

    def write_blog(self):
        print(“日付を入力してください”)
        self.date = input()
        print(“タイトルを入力してください”)
        self.title = input()
        print(“本文を入力してください”)
        self.contents = input()

    def show_blog(self):
        line = "\n---------------------------"
        print(“日付 : " + self.date + line)
        print("タイトル : " + self.title + line)
        print(“本文 : " + self.contents + line)

blog = Blog()
blog.write_blog()
blog.show_blog()
