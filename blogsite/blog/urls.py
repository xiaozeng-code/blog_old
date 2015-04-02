from django.conf.urls import patterns, url

#urlpatterns = patterns('',
#    url(r'^addType','blog.views.addType_',name='addType'),
#)



urlpatterns = patterns('blog.views',
    url(r'^home/$','home', name="home"),
    url(r'^talkfree/$','talkfree', name="talkfree"),
    url(r'^talkfree/(\d+)/$','talkdetail', name="detail"),
#    url(r'^logout/$','logout_', name="logout"),
#    url(r'^register/$','register_', name="register"),
#    url(r'^manage/$','manage',name='manage'),
#    url(r'^add/$','addBlog', name="add"),
#    url(r'^addType/$','addType_', name="add_type"),
)

