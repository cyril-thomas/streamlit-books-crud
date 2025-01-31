import sqlite3


def get_db_connection():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    conn.execute(
        """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    published_date TEXT,
    isbn TEXT UNIQUE
);
"""
    )
    conn.commit()
    conn.close()


def load_table_data():
    conn = get_db_connection()
    conn.execute(
        """ INSERT INTO books(id, title, author, published_date, isbn) VALUES 
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', '1925', '9780743273565'),
(2, 'To Kill a Mockingbird', 'Harper Lee', '1960', '9780061120084'),
(3, 'The Catcher in the Rye', 'J.D. Salinger', '1951', '9780316769488'),
(4, '1984', 'George Orwell', '1949', '9780451524935'),
(5, 'Pride and Prejudice', 'Jane Austen', '1813', '9781503290563'),
(6, 'The Hobbit', 'J.R.R. Tolkien', '1937', '9780547928227'),
(7, 'Moby Dick', 'Herman Melville', '1851', '9781503280786'),
(8, 'War and Peace', 'Leo Tolstoy', '1869', '9780199232765'),
(9, 'The Odyssey', 'Homer', 'Unknown', '9780140268867'),
(10, 'Crime and Punishment', 'Fyodor Dostoevsky', '1866', '9780486415871'),
(11, 'The Brothers Karamazov', 'Fyodor Dostoevsky', '1880', '9780374528379'),
(12, 'Brave New World', 'Aldous Huxley', '1932', '9780060850524'),
(13, 'Jane Eyre', 'Charlotte Bronte', '1847', '9780141441146'),
(14, 'Wuthering Heights', 'Emily Bronte', '1847', '9780141439556'),
(15, 'The Divine Comedy', 'Dante Alighieri', '1320', '9780142437223'),
(16, 'The Iliad', 'Homer', 'Unknown', '9780140275360'),
(17, 'Les Misérables', 'Victor Hugo', '1862', '9780451419439'),
(18, 'Anna Karenina', 'Leo Tolstoy', '1877', '9780143035008'),
(19, 'The Grapes of Wrath', 'John Steinbeck', '1939', '9780143039433'),
(20, 'The Lord of the Rings', 'J.R.R. Tolkien', '1954', '9780544003415'),
(21, 'The Alchemist', 'Paulo Coelho', '1988', '9780061122415'),
(22, 'Harry Potter and the Sorcerers Stone', 'J.K. Rowling', '1997', '9780590353427'),
(23, 'The Kite Runner', 'Khaled Hosseini', '2003', '9781594631931'),
(24, 'The Book Thief', 'Markus Zusak', '2005', '9780375842207'),
(25, 'The Chronicles of Narnia', 'C.S. Lewis', '1950', '9780066238500'),
(26, 'The Catch-22', 'Joseph Heller', '1961', '9781451626650'),
(27, 'The Road', 'Cormac McCarthy', '2006', '9780307387899'),
(28, 'Life of Pi', 'Yann Martel', '2001', '9780156027328'),
(29, 'The Shining', 'Stephen King', '1977', '9780307743657'),
(30, 'The Hunger Games', 'Suzanne Collins', '2008', '9780439023481'),
(31, 'The Fault in Our Stars', 'John Green', '2012', '9780525478812'),
(32, 'Gone Girl', 'Gillian Flynn', '2012', '9780307588371'),
(33, 'The Girl on the Train', 'Paula Hawkins', '2015', '9781594634024'),
(34, 'The Help', 'Kathryn Stockett', '2009', '9780399155345'),
(35, 'The Da Vinci Code', 'Dan Brown', '2003', '9780385504201'),
(36, 'Angels & Demons', 'Dan Brown', '2000', '9780671027360'),
(37, 'Inferno', 'Dan Brown', '2013', '9780385537858'),
(38, 'The Lost Symbol', 'Dan Brown', '2009', '9780385504225'),
(39, 'Digital Fortress', 'Dan Brown', '1998', '9780312263126'),
(40, 'Deception Point', 'Dan Brown', '2001', '9780671027384'),
(41, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', '2005', '9780307454546'),
(42, 'The Girl Who Played with Fire', 'Stieg Larsson', '2006', '9780307269980'),
(43, 'The Girl Who Kicked the Hornets Nest', 'Stieg Larsson', '2007', '9780307269997'),
(44, 'The Girl in the Spiders Web', 'David Lagercrantz', '2015', '9780385354288'),
(45, 'The Girl Who Takes an Eye for an Eye', 'David Lagercrantz', '2017', '9780451494320'),
(46, 'The Girl Who Lived', 'Christopher Greyson', '2017', '9781683993032'),
(47, 'The Silent Patient', 'Alex Michaelides', '2019', '9781250301697'),
(48, 'Where the Crawdads Sing', 'Delia Owens', '2018', '9780735219090'),
(49, 'Educated', 'Tara Westover', '2018', '9780399590504'),
(50, 'Becoming', 'Michelle Obama', '2018', '9781524763138'),
(51, 'The Nightingale', 'Kristin Hannah', '2015', '9780312577223'),
(52, 'All the Light We Cannot See', 'Anthony Doerr', '2014', '9781476746586'),
(53, 'The Goldfinch', 'Donna Tartt', '2013', '9780316055437'),
(54, 'The Handmaids Tale', 'Margaret Atwood', '1985', '9780385490818'),
(55, 'The Testaments', 'Margaret Atwood', '2019', '9780385543781'),
(56, 'Little Fires Everywhere', 'Celeste Ng', '2017', '9780735224292'),
(57, 'Big Little Lies', 'Liane Moriarty', '2014', '9780399167065'),
(58, 'The Light We Lost', 'Jill Santopolo', '2017', '9780735212756'),
(59, 'The Tattooist of Auschwitz', 'Heather Morris', '2018', '9780062797155'),
(60, 'The Alice Network', 'Kate Quinn', '2017', '9780062654199'),
(61, 'Before We Were Strangers', 'Renée Carlino', '2015', '9781501105777'),
(62, 'The Night Circus', 'Erin Morgenstern', '2011', '9780385534635'),
(63, 'The Martian', 'Andy Weir', '2011', '9780553418026'),
(64, 'Ready Player One', 'Ernest Cline', '2011', '9780307887443'),
(65, 'Artemis', 'Andy Weir', '2017', '9780553448122');"""
    )
    conn.commit()
    conn.close()


def add_book(title, author, published_date, isbn):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO books (title, author, published_date, isbn) VALUES (?, ?, ?, ?)",
        (title, author, published_date, isbn),
    )
    conn.commit()
    conn.close()


def get_all_books():
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return books


def get_book_by_id(book_id):
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM books WHERE id = ?", (book_id)).fetchone()
    conn.close()
    return book


def update_book(book_id, title, author, published_date, isbn):
    conn = get_db_connection()
    conn.execute(
        "UPDATE books SET title = ?, author = ?, published_date = ?, isbn = ? WHERE id = ?",
        (title, author, published_date, isbn, book_id),
    )
    conn.commit()
    conn.close()


def delete_book(book_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
