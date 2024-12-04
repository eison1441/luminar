from json import load
from collections import Counter
f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\books.json",encoding="UTF-8")
data=load(f)
all_book_name=[book.get("title") for book in data]
# print(all_book_name)

all_author_name=[book.get("author") for book in data]
# print(all_author_name)

spec_name=[book.get("title") for book in data if book.get("author")=="Delia Owens"]
# print(spec_name)

page_count={book.get("title"):book.get("pages") for book in data}
# print(page_count)
max_page=max(data,key=lambda book:book.get("pages")).get("title")
# print(f"{max_page} = {page_count.get(max_page)}")


price_of_book={book.get("title"):book.get("price") for book in data}

max_price=max(data,key=lambda book:book.get("price")).get("title")
# print(f"{max_price} = {price_of_book.get(max_price)}")

category=[book.get("genre") for book in data]
# print(category)
book_catogary_count={book.get("title"):len(book.get("genre",[] )) for book in data }
# print(frequent_category)
# print(book_catogary_count)
# max_catogary_count=max(data,key=lambda book:len(book.get("genre",[]))).get("genre")
# print(max_catogary_count,book_catogary_count.get(max_catogary_count))


# Extract genres
genres = [book['genre'] for book in data]

# Count occurrences of each genre
genre_count = Counter(genres)

# Find the most common genre
most_common_genre, most_common_count = genre_count.most_common(1)[0]

# Output the result
print(f"The most frequent genre is '{most_common_genre}' with {most_common_count} occurrences.")