from django.conf.urls import url

from users.views import UserDetail, Login, Signup, ActivateUser

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view(), name='detail'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^signup/$', Signup.as_view(), name='signup'),
    url(r'^activate/$', ActivateUser.as_view(), name='activate'),

]
