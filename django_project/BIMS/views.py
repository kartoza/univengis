# coding=UTF-8
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DataTableForm
from .models import DataTable, SlotData
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv


def index(request):
    return render(request, 'landing_page.html')

def file_upload(request):
    if request.method == 'POST':
        form = DataTableForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['document']
            reader = csv.reader(uploaded_file, delimiter=str(u':').encode('utf-8'))
            header = next(reader)
            for row in reader:
                    _, created = SlotData.objects.get_or_create(
                        object_id=row[0], shape=row[1], observer=row[2],
                        colect_no=row[3], colect_no_num=row[4], ob_date=row[5],
                        ob_hh=row[6], ob_mm=row[7], region=row[8],
                        major=row[9], loc_munic=row[10], minor=row[11],
                        park=row[12], centre_ed=row[13], precise=row[14],
                        site_code=row[15], notes=row[16], notes_2=row[17],
                        abundance=row[18], veg_type=row[19], habitat=row[20],
                        substrat=row[21], soile=row[22], moisture=row[23],
                        exposure=row[24], lithology=row[25], biotic_efe=row[26],
                        aspect=row[27], asp_no=row[28], asp_mag=row[29],
                        mag_decline=row[30], slope=row[31], slope_deg=row[32],
                        groth_form=row[33], sp_hait=row[34], spec_morf=row[35],
                        ob_type=row[36], ob_method=row[37], spes_tipe=row[38],
                        herb=row[39], p_name=row[40], name=row[41], sp_no=row[42],
                        sp_no_pre=row[43], grid_ref=row[44], pentad=row[45], alt=row[46],
                        point_x=row[47], point_y=row[48], point_z=row[49],
                        point_m=row[50], x_h=row[51], x_m=row[52], x_s=row[53],
                        y_h=row[54], y_m=row[55], y_s=row[56], c_year=row[57],
                        c_month=row[58], c_day=row[59], project=row[60], id_by=row[61],
                        verified=row[62], on_list=row[63], rd_status=row[64],
                        confidence=row[65], latitude=row[66], longitude=row[67],
                        data_admin=row[68], i_her_sout=row[69], need_id=row[70],
                        det_date=row[71], coll_p_no=row[72], ref=row[73], link2=row[74],
                        lat_long=row[75], datum=row[76])
            form.save()
            # return redirect('index')
    else:
        form = DataTableForm()
    slotdata = SlotData.objects.all()
    return render(request, 'upload.html', {
        'form': form, 'slotdata':slotdata,
    })

