from django.db import models
#django ma gotowy schemat logowania, poniższy import odpowiada za informacje użtkownika nazwę, hasło, mail
from django.contrib.auth.models import User


#nadanie atrybutów klasie Task
class Task(models.Model):
    #użytkownik, jeden użytkownik może mieć wiele zadań // relacja jeden do wielu // jeśli usuniemy użytkownika, jego zadania znikną// 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #tytuł zadania
    title = models.CharField(max_length=200, null=True, blank=True)
    #opis zadania
    description = models.TextField(null=True, blank=True)
    #czy zadanie ukończone // zadnie domyślnie nie zakończone
    complete = models.BooleanField(default=False)
    #utworzenie daty zadania
    create =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
#zrzuca zakończone zadania na koniec listy//sortowanie //
    class Meta:
        ordering = ['complete']