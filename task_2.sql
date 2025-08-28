CREATE TABLE Books(
  book_id INT PRIMARY KEY,
  title VARCHAR(130),
  author_id INT,
  price DOUBLE,
  publication_date DATE,
 FOREIGN KEY (author_id) REFERENCES Authors(author_id)
  
);
