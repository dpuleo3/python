from django import forms

from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.urls import reverse

# variable global
# tasks = ["kame", "hame", "ha"]

# form with client side validation 
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    
    priority = forms.IntegerField(label="Priority", min_value = 1, max_value = 10)

def index(request):
    #variable privada
    if "tasks" not in request.session:
        request.session["tasks"] = ["kame", "hame", "ha"]
    
    return render(request, "tasks/index.html", {
        
        "tasks": request.session["tasks"]
        
    })
    
# validaciones del form
def add(request):
    # chequea que se este ENVIANDO informacion
    if request.method == "POST":
        # va a contener toda la data que el cliente envie
        form = NewTaskForm(request.POST)
        
        # valida la informacion (server side validation)
        if form.is_valid():
            # se guarda el task enviado en el form en la variable task
            task = form.cleaned_data["task"]
            # se agrega task en la lista de tasks
            request.session["tasks"] += [task]
            # redirige a la pagina donde se vera la respuesta por eso el reverse
            return HttpResponseRedirect(reverse("tasks:index"))
        # si hay errores devuelve el mismo form para que vea en que se equivoco
        else:
            return render(request, "task/add.html", {
                "form": form
            })
            
    # si no envia informacion entonces solo se envia un form vacio
    return render(request, "tasks/add.html", {
        
        "form": NewTaskForm()
        
    })