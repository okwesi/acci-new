from django.shortcuts import render


# About Views
def about_History(request):
    return render(request, "acci_main/about/history.html")

def about_Founder(request):
    return render(request, "acci_main/about/founder.html")

def about_CoreValues(request):
    return render(request, "acci_main/about/core_values.html")

def about_Vision(request):
    return render(request, "acci_main/about/vision.html")
    
def about_Administration(request):
    return render(request, "acci_main/about/administration.html")
# end of About Views




#Leadership Views
def leadership_GeneralCouncil(request):
    return render(request, "acci_main/leadership/generalcouncil.html")

def leadership_Chairman(request):
    return render(request, "acci_main/leadership/chairman.html")

def leadership_GeneralSecretary(request):
    return render(request, "acci_main/leadership/generalsecretary.html")

def leadership_IMD(request):
    return render(request, "acci_main/leadership/imd.html")

def leadership_Heads(request):
    return render(request, "acci_main/leadership/heads.html")

def leadership_District(request):
    return render(request, "acci_main/leadership/district.html")

def leadership_Local(request):
    return render(request, "acci_main/leadership/local.html")
# End of Leadership 


# Ministries Views
def ministries_Children(request):
    return render(request, "acci_main/ministries/children.html")

def ministries_Youth(request):
    return render(request, "acci_main/ministries/youth.html")

def ministries_Men(request):
    return render(request, "acci_main/ministries/men.html")

def ministries_Women(request):
    return render(request, "acci_main/ministries/women.html")

def ministries_Aconsu(request):
    return render(request, "acci_main/ministries/aconsu.html")
# End of Ministries Views



# Missions Views

def missions_imd(request):
    return render(request, "acci_main/missions/imd.html")

def missions_board(request):
    return render(request, "acci_main/missions/board.html")
