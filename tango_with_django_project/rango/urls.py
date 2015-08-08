from django.conf.urls import patterns, url
from rango import views
from rango.views import index, about, category, add_category, add_page, register, user_login, restricted, user_logout
from django.conf import settings
from django.conf.urls.static import static

if not settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('',
		url(r'^$',views.index, name='index'),
		url(r'^about/', about, name='about'),
		url(r'^add_category/$',views.add_category,name='add_category'),
		url(r'^add_page/$',views.add_page,name='add_page'),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page,name='add_page'),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.category,name='category'),
		url(r'^register/$',views.register,name='register'),
		url(r'^login/$',views.user_login, name='login'),
		url(r'^restricted/',views.restricted,name='restricted'),
		url(r'^logout/$',views.user_logout, name='logout')
	)