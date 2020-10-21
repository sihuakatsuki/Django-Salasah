# Generated by Django 3.1.2 on 2020-10-18 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KodeBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_barang', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('no_telepon', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Varian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('harga_beli', models.IntegerField()),
                ('harga_jual', models.IntegerField()),
                ('berat', models.IntegerField(null=True)),
                ('deskripsi', models.TextField()),
                ('gambar', models.ImageField(upload_to='')),
                ('bahan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Salasah.bahan')),
                ('kategori', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Salasah.kategori')),
                ('kode_barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Salasah.kodebarang')),
                ('varian', models.ManyToManyField(to='Salasah.Varian')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat', models.TextField()),
                ('no_penerima', models.CharField(max_length=13)),
                ('kode_booking', models.CharField(max_length=30)),
                ('jasa_kirim', models.CharField(max_length=200)),
                ('tanggal', models.DateTimeField()),
                ('kode_barang', models.ManyToManyField(to='Salasah.KodeBarang')),
                ('penerima', models.ManyToManyField(to='Salasah.Toko')),
            ],
        ),
        migrations.CreateModel(
            name='Masuk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satuan', models.IntegerField()),
                ('keterangan', models.TextField()),
                ('tanggal', models.DateTimeField()),
                ('kode_barang', models.ManyToManyField(to='Salasah.KodeBarang')),
            ],
        ),
        migrations.CreateModel(
            name='Keluar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satuan', models.IntegerField()),
                ('keterangan', models.TextField()),
                ('tanggal', models.DateTimeField()),
                ('kode_barang', models.ManyToManyField(to='Salasah.KodeBarang')),
            ],
        ),
    ]