from django.urls import path
from.import views
urlpatterns = [
	path('',views.wedding_main_page, name='wedding_main_page'),
	path('reviews/',views.wedding_Review, name = 'wedding_Review'),
	path('Wedding_photo_shoot_view/<int:myid>',views.Wedding_photo_shoot_view,name='Wedding_photo_shoot_view'),
	path('wed_book_view/',views.wed_book_view,name='wed_book_view'),
	path('wed_shoot_view/',views.wed_shoot_view,name='wed_shoot_view'),
	path('contact/',views.contacts,name='contacts'),
	path('question/',views.questionViews,name='questionViews'),
	path('main_slider_show/',views.wed_main_slider_photo_show,name='wed_main_slider_photo_show'),
	path('main_slider_pic_detail_views/<int:myid>',views.Wedding_main_slider_detail_view,name='Wedding_main_slider_detail_view'),
	path('wed_shoot_view_full_view/<int:myid>',views.wed_shoot_view_full_view,name='wed_shoot_view_full_view'),
]
