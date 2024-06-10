class Book:
  all_books = []

  def __init__(self, title):
    if not title:
      raise Exception("Title cannot be empty")
    self.title = title
    Book.all_books.append(self)

  def get_title(self):
    return self.title

  @classmethod
  def get_all_books(cls):
    return cls.all_books

class Author:
  all_authors = []

  def __init__(self, name):
    if not name:
      raise Exception("Author name cannot be empty")
    self.name = name
    self.contracts = []
    Author.all_authors.append(self)

  def get_name(self):
    return self.name

  def get_contracts(self):
    return self.contracts

  def get_books(self):
    books = []
    for contract in self.contracts:
      books.append(contract.get_book())
    return books

  def sign_contract(self, book, date, royalties):
    if not date or not 0 <= royalties <= 100:
      raise Exception("Invalid contract details")
    contract = Contract(self, book, date, royalties)
    self.contracts.append(contract)
    return contract

  def total_royalties(self):
    total = 0
    for contract in self.contracts:
      total += contract.get_royalties()
    return total

  @classmethod
  def get_all_authors(cls):
    return cls.all_authors

class Contract:
  all_contracts = []

  def __init__(self, author, book, date, royalties):
    if not author or not book:
      raise Exception("Author and Book cannot be null")
    self.author = author
    self.book = book
    self.date = date
    self.royalties = royalties
    Contract.all_contracts.append(self)

  def get_author(self):
    return self.author

  def get_book(self):
    return self.book

  def get_date(self):
    return self.date

  def get_royalties(self):
    return self.royalties

  @classmethod
  def contracts_by_date(cls, date):
    return [contract for contract in cls.all_contracts if contract.get_date() == date]

# Test functions (assuming these are in a separate file)

def test_book_init():
  """Test Book class initializes with title"""
  book = Book(title="Title")
  assert book.get_title() == "Title"

def test_author_init():
  """Test Author class initializes with name"""
  author = Author(name="Name")
  assert author.get_name() == "Name"

def test_contract_init():
  """Test Contract class initializes with author, book, date, royalties"""
  book = Book(title="Title")
  author = Author(name="Name")
  contract = Contract(author, book, "2024-06-11",royalties, 50)
  assert contract.get_author() == author
  assert contract.get_book() == book
  assert contract.get_date() == "2024-06-11"
  assert contract.get_royalties() == 50

