# qa_python
Добавлены тесты на каждый метод класса BooksCollector
1. test_add_new_book (Тест на добавление новой книги "book 1")
2. test_add_new_book_with_invalid_name_false (Проверка, что книга, чье название больше 41 символов, не добавляется)
3. test_set_book_genre (Проверка, что жанр к книге назначается успешно)
4. test_set_book_genre_with_invalid_genre_false (Тест на добавление несуществующего жанра к книге)
5. test_get_book_genre (Тест на получение жанра книги)
6. test_get_books_with_specific_genre (Тест на вывод книг с определенным жанром, в данном случае с жанром "Фантастика")
7. test_get_books_genre (Тест на получение словаря books_genre)
8. test_get_books_for_children (Тест на проверку, что книга с жанром, не подходящим для детей, не возвращается)
9. test_add_book_in_favorites (Тест на добавление книги в избранное)
10. test_add_book_in_favorites_with_invalid_book_false (Тест, что несуществующая книга, не добавляется в избранное)
11. test_delete_book_from_favorites (Тест на удаление книги из избранного)
12. test_get_list_of_favorites_books (Тест на получение списка избранных книг)
