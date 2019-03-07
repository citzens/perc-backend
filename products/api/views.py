from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import ProductSerializer
from products.models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer