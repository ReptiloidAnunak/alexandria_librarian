from backend.loaders_api.openlibrary_books_loader import load_openlibrary_books_info
from data_base.management.base_manager import BaseManager
from data_base.models import BookStatus



# def run_app():
#     show_main_app_banner()
#     base_manager = BaseManager()
#     # load_openlibrary_books_info(base_manager)
#     # base_manager.delete_book_by_id(158155633564690996925116302685280854940)
#     # print(base_manager.load_books_objs_from_db())
#     # base_manager.change_book_status(61873012564104636441117030014172418739, BookStatus.issued.value)
#
# if __name__ == '__main__':
#     run_app()