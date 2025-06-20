# Generated by Django 3.2.11 on 2025-06-17 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(blank=True, choices=[('M', '男'), ('F', '女'), ('O', '其他')], max_length=1, verbose_name='性别')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='住址')),
                ('postal_code', models.CharField(blank=True, max_length=20, verbose_name='邮编')),
                ('residence_card_no', models.CharField(blank=True, max_length=50, verbose_name='在留卡号')),
                ('passport_no', models.CharField(blank=True, max_length=50, verbose_name='护照号')),
                ('last_login_time', models.DateTimeField(blank=True, null=True, verbose_name='最后登录时间')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='电话')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='邮箱')),
                ('contract_terminated', models.BooleanField(default=False, verbose_name='契约解除')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(choices=[('ZAI_RYU_KANJI', '在留卡汉字登记'), ('JUMIN_TOROKU', '住民登记'), ('INKAN_TOROKU', '个人印章登记'), ('JUMINHYO_ISSUE', '住民票发行'), ('INKAN_SHOMEI', '印章证明发行'), ('MYNUMBER_ISSUE', 'Mynumber卡发行'), ('MYNUMBER_UPDATE', 'Mynumber卡更新'), ('JPN_MOBILE', '日本手机号办理'), ('NET_SERVICE', '网络办理'), ('LANDLINE', '座机办理'), ('BANK_ACCOUNT', '个人银行开户'), ('CAPITAL_DEPOSIT', '资本金存入'), ('NON_RES_TO_RES', '非居住者变更居住者'), ('OFFICE_RENT', '法人事务所租赁'), ('COMPANY_SEAL_PURCHASE', '公司印章购买'), ('TAX_ACCOUNTANT', '税理士签约'), ('CORP_ACCOUNT_OPEN', '法人账户开户'), ('KOUSEI_NENKIN', '厚生年金等')], max_length=50, verbose_name='项目名称')),
                ('status', models.CharField(choices=[('APPLIED', '申请中'), ('PROCESSING', '处理中'), ('COMPLETED', '完成'), ('PAUSED', '暂停'), ('CANCELED', '取消')], default='APPLIED', max_length=20, verbose_name='状态')),
                ('application_date', models.DateField(blank=True, null=True, verbose_name='申请日')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='开始处理日')),
                ('completion_date', models.DateField(blank=True, null=True, verbose_name='完成日')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(choices=[('IMM_NAME_REG', '入管局汉字姓名登记'), ('HOUMU_DOCS', '法务局材料'), ('PENSION_DOCS', '年金材料'), ('OTHER', '其他')], max_length=50, verbose_name='材料类型')),
                ('generated_date', models.DateField(blank=True, null=True, verbose_name='生成日期')),
                ('status', models.CharField(blank=True, max_length=20, verbose_name='状态')),
                ('file_url', models.CharField(blank=True, max_length=255, verbose_name='文件链接')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, verbose_name='会社名')),
                ('representative', models.CharField(blank=True, max_length=100, verbose_name='法人代表')),
                ('contract_start', models.DateField(blank=True, null=True, verbose_name='契約开始日')),
                ('contract_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='契約金額')),
                ('establishment_date', models.DateField(blank=True, null=True, verbose_name='設立日')),
                ('company_address', models.CharField(blank=True, max_length=255, verbose_name='会社地址')),
                ('fiscal_year_end', models.DateField(blank=True, null=True, verbose_name='決算日')),
                ('seal_purchase_date', models.DateField(blank=True, null=True, verbose_name='印鑑購入日')),
                ('tax_filing_date', models.DateField(blank=True, null=True, verbose_name='税務新規申告日')),
                ('pension_join_date', models.DateField(blank=True, null=True, verbose_name='厚生年金加入日')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='給料')),
                ('tax_accountant', models.CharField(blank=True, max_length=100, verbose_name='税理士')),
                ('tax_contract_date', models.DateField(blank=True, null=True, verbose_name='税理士契約日')),
                ('corporate_account', models.CharField(blank=True, max_length=100, verbose_name='法人口座')),
                ('family_support', models.BooleanField(default=False, verbose_name='家族扶養')),
                ('employee_count', models.PositiveIntegerField(default=0, verbose_name='職員雇用数量')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='AdminClientPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorized_clients', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorized_admins', to='core.client')),
            ],
            options={
                'verbose_name': '管理员客户授权',
                'verbose_name_plural': '管理员客户授权',
                'unique_together': {('admin', 'client')},
            },
        ),
    ]
