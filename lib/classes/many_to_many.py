class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        
        self.__author = author
        self.__magazine = magazine
        self.__title = title

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine


        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self.__name = name
        self.__articles = []
        self.__magazines = set()

    @property
    def name(self):
        return self.__name

    def add_article(self, magazine, title):
        article = Article(title)
        self.__articles.append(article)
        self.__magazines.add(magazine)
        return article

    def articles(self):
        return self.__articles

    def magazines(self):
        return list(self.__magazines)

    def topic_areas(self):
        if not self.__articles:
            return None
        topics = set()
        for magazine in self.__magazines:
            topics.update(magazine.topic_areas)
        return list(topics)


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.__published_articles = []

    def add_article(self, article):
        self.__published_articles.append(article)

    def articles(self):
        return self.__published_articles

    def article_titles(self):
        if not self.__published_articles:
            return None
        return [article.title for article in self.__published_articles]

    def contributing_authors(self):
        if not self.__published_articles:
            return None
        
        author_counts = {}
        for article in self.__published_articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors
