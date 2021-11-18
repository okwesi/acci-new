from django.conf.urls import url
from . import views
from . import dropdownViews

urlpatterns = [
   
    # About urls
    url('history', dropdownViews.about_History, name="history"),
    url('founder', dropdownViews.about_Founder, name="founder"),
    url('core_values', dropdownViews.about_CoreValues, name="core_values"),
    url('vision', dropdownViews.about_Vision , name="vision"),
    url('administration', dropdownViews.about_Administration, name="administration"),
    # End of About Urls
    
    
    # Leadership urls
    url('chairman', dropdownViews.leadership_Chairman, name="chairman"),
    url('general_council', dropdownViews.leadership_GeneralCouncil, name="general_council"),
    url('general_secretary', dropdownViews.leadership_GeneralSecretary, name="general_secretary"),
    url('imd', dropdownViews.leadership_IMD, name="imd"),
    url('heads', dropdownViews.leadership_Heads, name="heads"),
    url('district', dropdownViews.leadership_District, name="district"),
    url('local', dropdownViews.leadership_Local, name="local"),
    # Emd of Leadership Url
    
    # Ministries Urls
    url('children', dropdownViews.ministries_Children, name="children"),
    url('youth', dropdownViews.ministries_Youth, name="youth"),
    url('men', dropdownViews.ministries_Men, name="men"),
    url('women', dropdownViews.ministries_Women, name="women"),
    url('aconsu', dropdownViews.ministries_Aconsu, name="aconsu"),
    # End of Ministries Url
    
    
    # Missions Url
    url('international-missions-directorate', dropdownViews.missions_imd, name="missions_imd"),
    url('missions-board', dropdownViews.missions_board, name="missions_board"),
    
]
