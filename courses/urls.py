from django.conf.urls import url
from .views import (CourseList,CourseDetail,CourseCreation,CourseUpdate,CourseDelete)

urlpatterns = [
    url(r'^$', CourseList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='detail'),
    url(r'^nuevo$', CourseCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name='delete'),
]