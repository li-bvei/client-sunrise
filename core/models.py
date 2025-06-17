from django.db import models
from django.contrib.auth.models import User


# 客户信息
class Client(models.Model):
    GENDER_CHOICES = [('M', '男'), ('F', '女'), ('O', '其他')]

    name = models.CharField("姓名", max_length=100)
    birthday = models.DateField("生日", null=True, blank=True)
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, blank=True)
    address = models.CharField("住址", max_length=255, blank=True)
    postal_code = models.CharField("邮编", max_length=20, blank=True)
    residence_card_no = models.CharField("在留卡号", max_length=50, blank=True)
    passport_no = models.CharField("护照号", max_length=50, blank=True)
    last_login_time = models.DateTimeField("最后登录时间", null=True, blank=True)
    phone = models.CharField("电话", max_length=20, blank=True)
    email = models.EmailField("邮箱", blank=True)
    contract_terminated = models.BooleanField("契约解除", default=False)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.name


# 管理员与客户权限映射表
class AdminClientPermission(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorized_clients')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='authorized_admins')

    class Meta:
        unique_together = ('admin', 'client')
        verbose_name = "管理员客户授权"
        verbose_name_plural = "管理员客户授权"

    def __str__(self):
        return f"{self.admin.username} -> {self.client.name}"


# 办理项目
class Project(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', '申请中'),
        ('PROCESSING', '处理中'),
        ('COMPLETED', '完成'),
        ('PAUSED', '暂停'),
        ('CANCELED', '取消'),
    ]

    PROJECT_CHOICES = [
        ('ZAI_RYU_KANJI', '在留卡汉字登记'),
        ('JUMIN_TOROKU', '住民登记'),
        ('INKAN_TOROKU', '个人印章登记'),
        ('JUMINHYO_ISSUE', '住民票发行'),
        ('INKAN_SHOMEI', '印章证明发行'),
        ('MYNUMBER_ISSUE', 'Mynumber卡发行'),
        ('MYNUMBER_UPDATE', 'Mynumber卡更新'),
        ('JPN_MOBILE', '日本手机号办理'),
        ('NET_SERVICE', '网络办理'),
        ('LANDLINE', '座机办理'),
        ('BANK_ACCOUNT', '个人银行开户'),
        ('CAPITAL_DEPOSIT', '资本金存入'),
        ('NON_RES_TO_RES', '非居住者变更居住者'),
        ('OFFICE_RENT', '法人事务所租赁'),
        ('COMPANY_SEAL_PURCHASE', '公司印章购买'),
        ('TAX_ACCOUNTANT', '税理士签约'),
        ('CORP_ACCOUNT_OPEN', '法人账户开户'),
        ('KOUSEI_NENKIN', '厚生年金等'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    project_name = models.CharField("项目名称", max_length=50, choices=PROJECT_CHOICES)
    status = models.CharField("状态", max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    application_date = models.DateField("申请日", null=True, blank=True)
    start_date = models.DateField("开始处理日", null=True, blank=True)
    completion_date = models.DateField("完成日", null=True, blank=True)
    remarks = models.TextField("备注", blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return f"{self.get_project_name_display()} - {self.client.name}"


# 公司信息
class Company(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="companies")
    company_name = models.CharField("会社名", max_length=200)
    representative = models.CharField("法人代表", max_length=100, blank=True)
    contract_start = models.DateField("契約开始日", null=True, blank=True)
    contract_amount = models.DecimalField("契約金額", max_digits=12, decimal_places=2, null=True, blank=True)
    establishment_date = models.DateField("設立日", null=True, blank=True)
    company_address = models.CharField("会社地址", max_length=255, blank=True)
    fiscal_year_end = models.DateField("決算日", null=True, blank=True)
    seal_purchase_date = models.DateField("印鑑購入日", null=True, blank=True)
    tax_filing_date = models.DateField("税務新規申告日", null=True, blank=True)
    pension_join_date = models.DateField("厚生年金加入日", null=True, blank=True)
    salary = models.DecimalField("給料", max_digits=10, decimal_places=2, null=True, blank=True)
    tax_accountant = models.CharField("税理士", max_length=100, blank=True)
    tax_contract_date = models.DateField("税理士契約日", null=True, blank=True)
    corporate_account = models.CharField("法人口座", max_length=100, blank=True)
    family_support = models.BooleanField("家族扶養", default=False)
    employee_count = models.PositiveIntegerField("職員雇用数量", default=0)
    remarks = models.TextField("备注", blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.company_name


# 材料记录
class Material(models.Model):
    MATERIAL_TYPES = [
        ('IMM_NAME_REG', '入管局汉字姓名登记'),
        ('HOUMU_DOCS', '法务局材料'),
        ('PENSION_DOCS', '年金材料'),
        ('OTHER', '其他'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='materials')
    material_type = models.CharField("材料类型", max_length=50, choices=MATERIAL_TYPES)
    generated_date = models.DateField("生成日期", null=True, blank=True)
    status = models.CharField("状态", max_length=20, blank=True)
    file_url = models.CharField("文件链接", max_length=255, blank=True)
    remarks = models.TextField("备注", blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return f"{self.get_material_type_display()} - {self.client.name}"
