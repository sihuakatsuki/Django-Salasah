from rest_framework import serializers
from .models import *

class KategoriSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class BahanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bahan
        fields = '__all__'     

class VarianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Varian
        fields = '__all__'       

class KodeBarangSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KodeBarang
        fields = '__all__'        

class ProdukSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produk
        fields = ('id', 'nama', 'harga_beli', 'harga_jual', 'kategori', 'bahan', 'berat', 'varian', 'deskripsi', 'kode_barang', 'gambar')

class MasukSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Masuk
        fields = '__all__'      

class KeluarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keluar
        fields = '__all__'   

class TokoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toko
        fields = '__all__'       

class OnlineOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OnlineOrder
        fields = '__all__'        

class OfflineOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OfflineOrder
        fields = '__all__'      