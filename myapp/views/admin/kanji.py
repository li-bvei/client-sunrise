
def kanji(request):
    if request.method == 'POST':
        # 生成 Saikoufu 数据的 PDF
        saikoufu_pdf_bytes = create_pdf_saikoufu_data(request.POST)

        # 生成 Kanji 数据的 PDF
        kanji_pdf_bytes = create_pdf_kanji_data(request.POST)

        # 创建一个 PdfWriter 对象来合并两个 PDF 文件
        output_pdf = io.BytesIO()
        pdf_writer = PdfWriter(output_pdf)

        # 添加 Saikoufu PDF 文件的页面
        pdf_writer.add_page(PdfReader(io.BytesIO(saikoufu_pdf_bytes)).pages[0])

        # 添加 Kanji PDF 文件的页面
        pdf_writer.add_page(PdfReader(io.BytesIO(kanji_pdf_bytes)).pages[0])

        # 将合并后的 PDF 写入输出 PDF 文件中
        pdf_writer.write(output_pdf)

        # 将合并后的 PDF 返回给用户
        response = HttpResponse(output_pdf.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="combined_pdf.pdf"'
        return response

    return render(request, 'form_kanji.html')

    
def create_pdf_saikoufu_data(data):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    pdfmetrics.registerFont(TTFont('hei', 'hei.ttf'))
    pdfmetrics.registerFont(TTFont('yumin', 'yumin.ttf'))
    # can.setFont("hei", 15)
    can.setFont("yumin", 15)
    date_value = data.get('age', '')

    # 将日期值按照'yy/mm/dd'格式分割成数组
    parts = date_value.split('-')
    print(parts)
    # 使用空格连接数组元素，得到格式转换后的日期字符串
    formatted_date = '         '.join(parts)
    can.drawAlignedString(saikoufu_coordinates['name11']['x'],saikoufu_coordinates['name11']['y'],data.get('name1', ''))
    can.drawAlignedString(saikoufu_coordinates['name22']['x'],saikoufu_coordinates['name22']['y'],data.get('name2', ''))
    can.drawAlignedString(saikoufu_coordinates['name33']['x'],saikoufu_coordinates['name33']['y'],data.get('name3', ''))
    can.drawAlignedString(saikoufu_coordinates['name44']['x'],saikoufu_coordinates['name44']['y'],data.get('name4', ''))
    can.drawAlignedString(saikoufu_coordinates['age']['x'],saikoufu_coordinates['age']['y'],formatted_date)

    # 绘制性别男

    male = data.get('male','')
    if male == 'malex':
        # 绘制性别男
        can.circle(saikoufu_coordinates['malex']['x'], saikoufu_coordinates['malex']['y'], saikoufu_coordinates['malex']['size'],stroke=1, fill=0)

    elif male == 'maley':
        # 绘制性别女
        can.circle(saikoufu_coordinates['maley']['x'], saikoufu_coordinates['maley']['y'], saikoufu_coordinates['maley']['size'],stroke=1, fill=0)


    # 国籍
    can.drawAlignedString(saikoufu_coordinates['nation']['x'],saikoufu_coordinates['nation']['y'],data.get('nation', ''))
    
    can.drawAlignedString(saikoufu_coordinates['liyou']['x'],saikoufu_coordinates['liyou']['y'],data.get('liyou', ''))
    
    can.drawAlignedString(saikoufu_coordinates['zairyuid']['x'],saikoufu_coordinates['zairyuid']['y'],data.get('zairyuid', ''))

    can.drawAlignedString(saikoufu_coordinates['address']['x'],saikoufu_coordinates['address']['y'],data.get('address', ''))
    # 家庭电话
    can.drawAlignedString(saikoufu_coordinates['family_tel']['x'],saikoufu_coordinates['family_tel']['y'],data.get('family_tel',''))
    # 家庭手机
    can.drawAlignedString(saikoufu_coordinates['family_phone']['x'],saikoufu_coordinates['family_phone']['y'],data.get('family_phone',''))




    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)

    existing_pdf = PdfReader(open(r'G:\work\sunrise\py\pdffile\再交付.pdf', "rb"))

    output = PdfWriter()
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    final_pdf = io.BytesIO()
    output.write(final_pdf)
    final_pdf.seek(0)
    return final_pdf.getvalue()