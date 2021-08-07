from rest_framework import generics
from products.models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pass


class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pass

class ProductGetByCondition(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        tc = self.request.GET.get('treatment_type')
        return Product.objects.filter(treatment_type=tc)