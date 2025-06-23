from django.db import models


class BasicIdentity(models.Model):
    katakana = models.CharField("カタカナ", max_length=100, blank=True, null=True)
    passport_number = models.CharField("护照号", max_length=50, blank=True, null=True)
    name = models.CharField("姓名", max_length=100, blank=True, null=True)
    birthday = models.DateField("誕生日", blank=True, null=True)
    passport_expiry = models.DateField("护照有效期", blank=True, null=True)
    phone = models.CharField("电话", max_length=30, blank=True, null=True)
    postal_code = models.CharField("郵便番号", max_length=20, blank=True, null=True)
    address = models.CharField("住址", max_length=255, blank=True, null=True)
    residence_card_number = models.CharField("在留卡号", max_length=50, blank=True, null=True)
    residence_card_expiry = models.DateField("在留有效期", blank=True, null=True)
    mynumber = models.CharField("Mynumber", max_length=50, blank=True, null=True)
    entry_date = models.DateField("入境时间", blank=True, null=True)

    def __str__(self):
        return f"{self.name or '无名'} - {self.passport_number or '无护照号'}"


class Thing(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)           # 客户名称
    birthday = models.CharField(max_length=20, blank=True, null=True)        # 生日
    address = models.CharField(max_length=255, blank=True, null=True)        # 地址
    companyName = models.CharField(max_length=255, blank=True, null=True)    # 公司名称
    taxAdvisor = models.CharField(max_length=100, blank=True, null=True)     # 公司税理士
    customerType = models.CharField(max_length=50, blank=True, null=True)    # 客户类型
    remark = models.CharField(max_length=255, blank=True, null=True)         # 备注
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "core_thing"


class Dependent(models.Model):
    basic_identity = models.ForeignKey(
        BasicIdentity,
        on_delete=models.CASCADE,
        related_name='dependents',
        verbose_name="所属客户"
    )

    katakana = models.CharField("カタカナ", max_length=100, blank=True, null=True)
    name = models.CharField("姓名", max_length=100, blank=True, null=True)
    relationship = models.CharField("与本人关系", max_length=50, blank=True, null=True)
    birthday = models.DateField("誕生日", blank=True, null=True)
    phone = models.CharField("电话", max_length=30, blank=True, null=True)

    residence_card_number = models.CharField("在留卡号", max_length=50, blank=True, null=True)
    status_of_residence = models.CharField("在留资格", max_length=50, blank=True, null=True)
    residence_card_expiry = models.DateField("在留有效期", blank=True, null=True)

    my_number = models.CharField("マイナンバー", max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name or '无名'}（{self.relationship or '无关系'}）"
    class Meta:
        db_table = "core_Dependent"
