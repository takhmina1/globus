from django.urls import path
from .views import UserListView, ProductListView, OrderListView
from django.urls import path
from .views import (
    ProductCategoryListCreateView, ProductCategoryDetailView,
    HistoryListCreateView, HistoryDetailView,
    ShoppingCartListCreateView, ShoppingCartDetailView
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('product-categories/', ProductCategoryListCreateView.as_view(), name='product-category-list-create'),
    path('product-categories/<int:pk>/', ProductCategoryDetailView.as_view(), name='product-category-detail'),

    path('history/', HistoryListCreateView.as_view(), name='history-list-create'),
    path('history/<int:pk>/', HistoryDetailView.as_view(), name='history-detail'),

    path('shopping-cart/', ShoppingCartListCreateView.as_view(), name='shopping-cart-list-create'),
    path('shopping-cart/<int:pk>/', ShoppingCartDetailView.as_view(), name='shopping-cart-detail'),
]




