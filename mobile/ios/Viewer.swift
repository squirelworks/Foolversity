// iOS scaffold. Swift.
// Calls the translated core. Does not build.

import Foundation

struct Page {
    let id: String
    let text: [String]
    let items: [[String: String]]
}

struct Book {
    let title: String
    let pages: [Page]
}

// Translated from shared/core.py
func loadBook(path: String) -> Book {
    // read JSON, map to Book
    return Book(title: "", pages: [])
}

func pageAt(book: Book, index: Int) -> Page? {
    guard index >= 0 && index < book.pages.count else { return nil }
    return book.pages[index]
}

// Shell
class Viewer {
    var book: Book?
    var index = 0

    func open(path: String) {
        book = loadBook(path: path)
        index = 0
    }

    func current() -> Page? {
        guard let book = book else { return nil }
        return pageAt(book: book, index: index)
    }
}
