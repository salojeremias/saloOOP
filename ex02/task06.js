const book = {
    isbn: "13-978-0156012195",
    name: "The Little Prince",
    author: "Antoine De Saint-Exupéry",
    publicationDate: "March 5, 2013",
    getAuthors: function() {
        return this.getAuthors.join(", ");
    },
    setAuthors: function(newAuthors) {
        this.authors = Array.isArray(newAuthors) ? newAuthors : [newAuthors];
    },
    getIsbn: function() {
        return this.isbn;
    },
    setIsbn: function(newIsbn) {
        this.isbn = newIsbn;
    },
};

const book1 = {
    isbn: "13-978-0156012195",
    name: "The Little Prince",
    author: "Antoine De Saint-Exupéry",
    publicationDate: "March 5, 2013",
};

const book2 = {
    isbn: "9789510425428",
    name: "Mielensäpahoittaja",
    author: "Tuomas Kyrö",
    publicationDate: "June 1, 2010",
};

// check for the same isbn
if (book1.isbn === book2.isbn) {
    console.log("Books have the same model.");
} else {
    console.log("They are different books.");
}

// check for the same identity
if (book1 === book2) {
    console.log("Books have the same identity.")
} else {
    console.log("Books have different identities.")
}