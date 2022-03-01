from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mall import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('Product', views.ProductView, 'Product')


class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class HelloReact1(TemplateView):
    template_name = 'React101/HelloReact1.html'


class HelloReact2(TemplateView):
    template_name = 'React101/HelloReact2.html'


class HelloReact3(TemplateView):
    template_name = 'React101/HelloReact3.html'


class HelloReact4(TemplateView):
    template_name = 'React101/HelloReact4.html'


class HelloReact5(TemplateView):
    template_name = 'React101/HelloReact5.html'


class HelloReact(TemplateView):
    def __init__(self, temp_name):
        super().__init__()
        self.template_name = temp_name


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('HelloReact1/', HelloReact('React101/HelloReact1.html').as_view(), name='React1'),
    path('HelloReact2/', HelloReact2.as_view(), name='React2'),
    path('HelloReact3/', HelloReact3.as_view(), name='React3'),
    path('HelloReact4/', HelloReact4.as_view(), name='React4'),
    path('HelloReact5/', HelloReact5.as_view(), name='React5'),
    # path('HelloReact6/', HelloReact6.as_view(), name='React6'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
