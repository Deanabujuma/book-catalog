This failure showed that my test correctly detects when books stored in the database are no longer displayed on the Books page.
## Question 1

The `Book` model carries a `ForeignKey` that points to `Publisher` because each book belongs to one publisher, while one publisher can have many books. If I reversed the relationship, I would be saying that each publisher belongs to one book, which would not match the structure of the catalog or the data I entered.

## Question 2

I used an `IntegerField` for `publication_year` because a year is a numeric value rather than regular text. If I stored it as a `CharField`, Django would treat the year as text, which would make numeric validation and comparisons less meaningful.