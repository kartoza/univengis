# coding=UTF-8
"""BIMS models."""
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
import csv
from collections import defaultdict


class SlotData(models.Model):
    """SlotData represents each row of the DataTable."""

    object_id = models.CharField(
        max_length=50,
        verbose_name=_('OBJECTID'),
        blank=True,
    )
    shape = models.CharField(
        max_length=250,
        verbose_name=_('Shape'),
        blank=True,
    )
    observer = models.CharField(
        max_length=100,
        verbose_name=_('Observer'),
        blank=True,
    )
    colect_no = models.CharField(
        max_length=50,
        verbose_name=_('COLECT_NO'),
        blank=True,
    )
    colect_no_num = models.CharField(
        max_length=50,
        verbose_name=_('COLECT_NO_NUM'),
        blank=True,
    )
    ob_date = models.CharField(
        verbose_name=_('OB_Date'),
        max_length=50,
        blank=True,)
    ob_hh = models.CharField(
        max_length=50,
        verbose_name=_('OB_HH'),
        blank=True,
    )
    ob_mm = models.CharField(
        max_length=50,
        verbose_name=_('OB_MM'),
        blank=True,
    )
    region = models.CharField(
        max_length=100,
        verbose_name=_('Region'),
    )
    major = models.CharField(
        max_length=100,
        verbose_name=_('MAJOR'),
        blank=True,
    )
    loc_munic = models.CharField(
        max_length=250,
        verbose_name=_('Loc_Munic'),
        blank=True,
    )
    minor = models.CharField(
        max_length=100,
        verbose_name=_('MINOR'),
        blank=True,
    )
    park = models.CharField(
        max_length=250,
        verbose_name=_('Park'),
        blank=True,
    )
    centre_ed = models.CharField(
        max_length=250,
        verbose_name=_('Centre_ED'),
        blank=True,
    )
    precise = models.TextField(
        verbose_name=_('PRECISE'),
        blank=True,
        max_length=500,
    )
    site_code = models.CharField(
        max_length=250,
        verbose_name=_('Site_code'),
        blank=True,
    )
    notes = models.TextField(
        max_length=1000,
        verbose_name=_('NOTES'),
        blank=True,
    )
    notes_2 = models.TextField(
        max_length=1000,
        verbose_name=_('NOTES_2'),
        blank=True,
    )
    abundance = models.CharField(
        max_length=250,
        verbose_name=_('Abundance'),
        blank=True,
    )
    veg_type = models.CharField(
        max_length=100,
        verbose_name=_('VEG_TYPE'),
        blank=True,
    )
    habitat = models.CharField(
        max_length=250,
        verbose_name=_('Habitat'),
        blank=True,
    )
    substrat = models.CharField(
        max_length=250,
        verbose_name=_('SUBSTRAT'),
        blank=True,
    )
    soile = models.CharField(
        max_length=250,
        verbose_name=_('SOILE'),
        blank=True,
    )
    moisture = models.CharField(
        max_length=250,
        verbose_name=_('MOISTURE'),
        blank=True,
    )
    exposure = models.CharField(
        max_length=250,
        verbose_name=_('EXPOSURE'),
        blank=True,
    )
    lithology = models.CharField(
        max_length=250,
        verbose_name=_('LITHOLOGY'),
        blank=True,
    )
    biotic_efe = models.CharField(
        max_length=250,
        verbose_name=_('Biotic_Efe'),
        blank=True,
    )
    aspect = models.CharField(
        max_length=100,
        verbose_name=_('ASPECT'),
        blank=True,
    )
    asp_no = models.CharField(
        max_length=100,
        verbose_name=_('Asp_no'),
        blank=True,
    )
    asp_mag = models.CharField(
        max_length=100,
        verbose_name=_('Asp_mag'),
        blank=True,
    )
    mag_decline = models.CharField(
        max_length=100,
        verbose_name=_('Mag_decline'),
        blank=True,
    )
    slope = models.CharField(
        max_length=250,
        verbose_name=_('SLOPE'),
        blank=True,
    )
    slope_deg = models.CharField(
        max_length=250,
        verbose_name=_('Slope_deg'),
        blank=True,
    )
    groth_form = models.CharField(
        max_length=250,
        verbose_name=_('GROTH_FORM'),
        blank=True,
    )
    sp_hait = models.CharField(
        max_length=30, blank=True, verbose_name=_('SP_HAIT'))
    spec_morf = models.CharField(
        max_length=250,
        verbose_name=_('SPEC_MORF'),
        blank=True,
    )
    ob_type = models.CharField(
        max_length=250,
        verbose_name=_('OB_type'),
        blank=True,
    )
    ob_method = models.CharField(
        max_length=250,
        verbose_name=_('OB_method'),
        blank=True,
    )
    spes_tipe = models.CharField(
        max_length=250,
        verbose_name=_('SPES_TIPE'),
        blank=True,
    )
    herb = models.CharField(
        max_length=250,
        verbose_name=_('Herb'),
        blank=True,
    )
    p_name = models.CharField(
        max_length=250,
        verbose_name=_('p_name'),
        blank=True,
    )
    name = models.TextField(
        max_length=500,
        verbose_name=_('name'),
        blank=True,
    )
    sp_no = models.CharField(
        max_length=100,
        verbose_name=_('sp_no'),
        blank=True,
    )
    sp_no_pre = models.CharField(
        max_length=100,
        verbose_name=_('sp_no_PRE'),
        blank=True,
    )
    grid_ref = models.CharField(
        max_length=100,
        verbose_name=_('Grid_Ref'),
        blank=True,
    )
    pentad = models.CharField(
        max_length=100,
        verbose_name=_('PENTAD'),
        blank=True,
    )
    alt = models.CharField(
        max_length=100,
        verbose_name=_('alt'),
        blank=True,
    )
    point_x = models.CharField(
        verbose_name=_('POINT_X'),
        blank=True,
        max_length=10,
    )
    point_y = models.CharField(
        verbose_name=_('POINT_Y'),
        blank=True,
        max_length=10,
    )
    point_z = models.CharField(
        verbose_name=_('POINT_Z'),
        blank=True,
        max_length=10,
    )
    point_m = models.CharField(
        verbose_name=_('POINT_M'),
        blank=True,
        max_length=10,
    )
    x_h = models.CharField(
        verbose_name=_('x_h'),
        blank=True,
        max_length=10,
    )
    x_m = models.CharField(
        verbose_name=_('x_m'),
        blank=True,
        max_length=10,
    )
    x_s = models.CharField(
        verbose_name=_('x_s'),
        blank=True,
        max_length=10,
    )
    y_h = models.CharField(
        verbose_name=_('y_h'),
        blank=True,
        max_length=10,
    )
    y_m = models.CharField(
        verbose_name=_('y_m'),
        blank=True,
        max_length=10,
    )
    y_s = models.CharField(
        verbose_name=_('y_s'),
        blank=True,
        max_length=10,
    )
    c_year = models.CharField(
        max_length=10,
        verbose_name=_('c_year'),
        blank=True,
    )
    c_month = models.CharField(
        max_length=10,
        verbose_name=_('c_month'),
        blank=True,
    )
    c_day = models.CharField(
        max_length=10,
        verbose_name=_('c_day'),
        blank=True,
    )
    project = models.CharField(
        max_length=250,
        verbose_name=_('Project'),
        blank=True,
    )
    id_by = models.CharField(
        max_length=250,
        verbose_name=_('ID_By'),
        blank=True,
    )
    verified = models.CharField(
        max_length=250,
        verbose_name=_('Verified'),
        blank=True,
    )
    on_list = models.CharField(
        max_length=100,
        verbose_name=_('on_list'),
        blank=True,
    )
    rd_status = models.CharField(
        max_length=100,
        verbose_name=_('RD_status'),
        blank=True,
    )
    confidence = models.CharField(
        max_length=100,
        verbose_name=_('Confidence'),
        blank=True,
    )
    latitude = models.CharField(
        max_length=100,
        verbose_name=_('LATITUDE'),
        blank=True,
    )
    longitude = models.CharField(
        max_length=100,
        verbose_name=_('LONGITUDE'),
        blank=True,
    )
    data_admin = models.CharField(
        max_length=100,
        verbose_name=_('Data_admin'),
        blank=True,
    )
    i_her_sout = models.CharField(
        max_length=100,
        verbose_name=_('I_HER_SOUT'),
        blank=True,
    )
    need_id = models.CharField(
        max_length=100,
        verbose_name=_('NEED_ID'),
        blank=True,
    )
    det_date = models.CharField(
        max_length=100,
        verbose_name=_('Det_date'),
        blank=True,
    )
    coll_p_no = models.CharField(
        max_length=100,
        verbose_name=_('COLL_P_NO'),
        blank=True,
    )
    ref = models.CharField(
        max_length=250,
        verbose_name=_('Ref'),
        blank=True,
    )
    link2 = models.CharField(
        max_length=250,
        verbose_name=_('link2'),
        blank=True,
    )
    lat_long = models.CharField(
        max_length=250,
        verbose_name=_('latlong'),
        blank=True,
    )
    datum = models.CharField(
        max_length=250,
        verbose_name=_('datum'),
        blank=True,
    )

    class Meta:
        verbose_name = _('Slot Data')
        ordering = ['pk']

    def __str__(self):
        return self.object_id

    def save(self, *args, **kwargs):
        super(SlotData, self).save(*args, **kwargs)


class DataTable(models.Model):
    """DataTable model gets data from a file csv."""

    table_name = models.CharField(
        max_length=250,
        verbose_name=_('Name of the Table'),
    )

    class Meta:
        verbose_name = _('Data Table')

    def __str__(self):
        return self.table_name

    def save(self, *args, **kwargs):
        # csv file is hardcorded because the upload form is not yet ready.
        # the csv file is loaded when object datatable is saved.
        with open('BIMS/media/uploads/Data_Sheet.csv') as file:
            reader = csv.reader(file)
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

        super(DataTable, self).save(*args, **kwargs)
