// Android / LineageOS scaffold. Kotlin.
// Calls the translated core. Does not build.

data class Page(
    val id: String,
    val text: List<String>,
    val items: List<Map<String, String>>
)

data class Book(
    val title: String,
    val pages: List<Page>
)

// Translated from shared/core.py
fun loadBook(path: String): Book {
    // read JSON, map to Book
    return Book("", emptyList())
}

fun pageAt(book: Book, index: Int): Page? {
    if (index < 0 || index >= book.pages.size) return null
    return book.pages[index]
}

// Shell
class Viewer {
    var book: Book? = null
    var index = 0

    fun open(path: String) {
        book = loadBook(path)
        index = 0
    }

    fun current(): Page? {
        val b = book ?: return null
        return pageAt(b, index)
    }
}
