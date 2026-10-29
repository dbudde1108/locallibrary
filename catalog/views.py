from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Author, Book, BookInstance, Genre
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = (
        BookInstance.objects.filter(status__exact="a").count()
    )

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Challenge - Genre and word filter
    num_genre = Genre.objects.all().count()
    num_genre_filtered = Genre.objects.filter(name__icontains="the").count()
    num_books_filtered = Book.objects.filter(title__icontains="the").count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genre": num_genre,
        "num_genre_filtered": num_genre_filtered,
        "num_books_filtered": num_books_filtered,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .select_related('book', 'borrower')
            .order_by('due_back')
        )
