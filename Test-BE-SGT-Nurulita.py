from datetime import datetime

#TASK 1
def tenYears(books):
    yearNow = datetime.now().year
    return[book for book in books if book['year']>= yearNow - 10]

books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925, 'genre': 'Fiction'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'genre': 'Fiction'},
    {'title': '1984 Romance', 'author': 'George Orwell', 'year': 1949, 'genre': 'Science Fiction'},
    {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'year': 2008, 'genre': 'Science Fiction'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813, 'genre': 'Romance'}
]

bookResult = tenYears(books)
print("Novel terbit 10 tahun terakhir :",bookResult)

#TASK2
def searchBooks(books, word):
    word = word.lower()
    return[book for book in books if (word in book['title'].lower() or
                                      word in book['author'].lower() or
                                      word in book['genre'].lower())]

searchResult = searchBooks(books, 'romance')
print("Hasil pencarian :",searchResult)

#NO.2
def ratingByGenre(books2):
    bookSort = sorted(books2, key=lambda x: (x['genre'],-x['rating']))
    return bookSort

books2 = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925, 'genre': 'Fiction', 'rating': 4.5},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'genre': 'Fiction', 'rating': 4.9},
    {'title': '1984', 'author': 'George Orwell', 'year': 1949, 'genre': 'Science Fiction', 'rating': 4.2},
    {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'year': 2008, 'genre': 'Science Fiction', 'rating': 4.6},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813, 'genre': 'Romance', 'rating': 4.7},
    {'title': 'Jane Eyre', 'author': 'Charlotte Bronte', 'year': 1847, 'genre': 'Romance', 'rating': 4.3},
    {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'year': 2003, 'genre': 'Mystery', 'rating': 3.9},
    {'title': 'Murder on the Orient Express', 'author': 'Agatha Christie', 'year': 1934, 'genre': 'Mystery', 'rating': 4.1},
    {'title': 'The Name of the Rose', 'author': 'Umberto Eco', 'year': 1980, 'genre': 'Mystery', 'rating': 4.4}
]

filterResult = ratingByGenre(books2)
print("Urutan buku :",filterResult)

#NO.3
def calculate(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            total = matrix[i][j]
            pos = [
                (i-1, j), (i+1, j),     # vertikal
                (i, j-1), (i, j+1),     # horizontal
                (i-1, j-1), (i-1, j+1), # diagonal atas
                (i+1, j-1), (i+1, j+1)  # diagonal bawah
            ]

            # Menjumlahkan nilai dari sel dan tetangga
            for x, y in pos:
                if 0 <= x < rows and 0 <= y < cols:
                    total += matrix[x][y]

            result[i][j] = total

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mathResult = calculate(matrix)

# Menampilkan hasil akhir
for row in mathResult:
    print(row)


#NO.4
def graduation(gpa, total_credit, honor_credit):
    if total_credit < 180 or gpa < 2.0:
        return "not graduating"

    if 2.0 <= gpa < 3.6:
        return "graduating"
    elif 3.6 <= gpa < 3.8:
        if honor_credit < 15:
            return "cum laude"
        elif honor_credit >= 15:
            return "magna cum laude"
    else:
        if honor_credit < 15:
            return "magna cum laude"
        elif honor_credit >= 15:
            return "summa cum laude"

print(graduation(3.87, 178, 16)) 
print(graduation(1.5, 199, 30))    
print(graduation(2.7, 380, 50))    
print(graduation(3.62, 200, 20))   
print(graduation(3.93, 185, 0))    
print(graduation(3.85, 190, 15))

#NO.5
def cheerleader(lines,num):
    for i in range(lines):
        spasi = ' '*i
        cheer = "Go" + (" Team Go"*(num-1))
        print(spasi+cheer)
        
cheerleader(2, 1)
print()
cheerleader(4, 3)
print()
cheerleader(2, 4)