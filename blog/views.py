from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Note


class Home(generic.ListView):
    model = Note

    template_name = 'blog_main.html'

    def get_queryset(self):
        return Note.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NoteCreate(generic.CreateView):
    model = Note
    fields = ['title', 'description', 'image', 'is_published']
    template_name = 'create_note.html'
    success_url = reverse_lazy('blog:blog_main')

class NoteDetail(generic.DetailView):
    model = Note
    template_name = 'detail_note.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        obj.views_count += 1
        obj.save(update_fields=['views_count'])

        if obj.views_count == 100:
            self.send_email(obj)

        return obj

    def send_email(self, note):
        subject = 'Поздравляем! Вы набрали 100 просмотров!'
        message = f'Ваша заметка "{note.title}" набрала 100 просмотров!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = (settings.SERVER_EMAIL,)

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )

class NoteUpdate(generic.UpdateView):
    model = Note
    fields = ['title', 'description', 'image', 'is_published']
    template_name = 'update_note.html'

    def get_success_url(self):
        return reverse_lazy('blog:detail_note', kwargs={'pk': self.object.pk})

class NoteDelete(generic.DeleteView):
    model = Note
    template_name = 'delete_note.html'
    success_url = reverse_lazy('blog:blog_main')
