# Generated by Django 3.2.11 on 2024-05-22 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='ad/')),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'b_ad',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'b_classification',
            },
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('method', models.CharField(blank=True, max_length=10, null=True)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('log_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'b_error_log',
            },
        ),
        migrations.CreateModel(
            name='Honkon_base',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vendor', models.CharField(max_length=255, verbose_name='商家')),
                ('product', models.CharField(max_length=255, verbose_name='商品')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
            ],
            options={
                'db_table': 'Honkon_base',
            },
        ),
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('ua', models.CharField(blank=True, max_length=200, null=True)),
                ('log_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'b_login_log',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'b_notice',
            },
        ),
        migrations.CreateModel(
            name='OpLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('re_ip', models.CharField(blank=True, max_length=100, null=True)),
                ('re_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('re_url', models.CharField(blank=True, max_length=200, null=True)),
                ('re_method', models.CharField(blank=True, max_length=10, null=True)),
                ('re_content', models.CharField(blank=True, max_length=200, null=True)),
                ('access_time', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'b_op_log',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='日期')),
                ('vendor', models.CharField(max_length=255, verbose_name='商家')),
                ('product', models.CharField(max_length=255, verbose_name='商品')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='合计')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'b_tag',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('role', models.CharField(blank=True, max_length=2, null=True)),
                ('status', models.CharField(choices=[('0', '正常'), ('1', '封号')], default='0', max_length=1)),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('avatar', models.FileField(null=True, upload_to='avatar/')),
                ('mobile', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', '男'), ('F', '女')], max_length=1, null=True)),
                ('description', models.TextField(max_length=200, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('push_email', models.CharField(blank=True, max_length=40, null=True)),
                ('push_switch', models.BooleanField(blank=True, default=False, null=True)),
                ('admin_token', models.CharField(blank=True, max_length=32, null=True)),
                ('token', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'b_user',
            },
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('xuehao', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.CharField(blank=True, max_length=20, null=True)),
                ('jiguan', models.CharField(blank=True, max_length=20, null=True)),
                ('sfz', models.CharField(blank=True, max_length=20, null=True)),
                ('minzu', models.CharField(blank=True, max_length=20, null=True)),
                ('remark', models.CharField(blank=True, max_length=30, null=True)),
                ('cover', models.ImageField(null=True, upload_to='cover/')),
                ('status', models.CharField(choices=[('0', '上架'), ('1', '下架')], default='0', max_length=1)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classification_thing', to='myapp.classification')),
                ('tag', models.ManyToManyField(blank=True, to='myapp.Tag')),
            ],
            options={
                'db_table': 'b_thing',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('record_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('classification', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classification', to='myapp.classification')),
                ('thing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thing_record', to='myapp.thing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_record', to='myapp.user')),
            ],
            options={
                'db_table': 'b_record',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('comment_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('like_count', models.IntegerField(default=0)),
                ('thing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thing_comment', to='myapp.thing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to='myapp.user')),
            ],
            options={
                'db_table': 'b_comment',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='banner/')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('thing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thing_banner', to='myapp.thing')),
            ],
            options={
                'db_table': 'b_banner',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=30, null=True)),
                ('desc', models.CharField(blank=True, max_length=300, null=True)),
                ('default', models.BooleanField(blank=True, default=False, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to='myapp.user')),
            ],
            options={
                'db_table': 'b_address',
            },
        ),
    ]
