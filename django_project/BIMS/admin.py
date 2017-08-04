# coding=UTF-8
"""Model admin class definitions."""

from django.contrib import admin
from .models import DataTable, SlotData

class SlotDataAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'shape', 'observer', 'colect_no', 'colect_no_num',
                    'ob_date', 'ob_hh', 'ob_mm', 'region', 'major', 'loc_munic',
                    'minor', 'park', 'centre_ed', 'precise', 'site_code', 'notes',
                    'notes_2', 'abundance', 'veg_type', 'habitat', 'substrat',
                    'soile', 'moisture', 'exposure', 'lithology', 'biotic_efe',
                    'aspect', 'asp_no', 'asp_mag', 'mag_decline', 'slope',
                    'slope_deg', 'groth_form', 'sp_hait', 'spec_morf',
                    'ob_type', 'ob_method', 'spes_tipe', 'herb', 'p_name',
                    'name', 'sp_no', 'sp_no_pre', 'grid_ref', 'pentad',
                    'alt', 'point_x', 'point_y', 'point_z', 'point_m',
                    'x_h', 'x_m', 'x_s', 'y_h', 'y_m', 'y_s', 'c_year', 'c_month',
                    'c_day', 'project', 'id_by',
                    'verified', 'on_list', 'rd_status',
                    'confidence', 'latitude', 'longitude',
                    'data_admin', 'i_her_sout', 'need_id',
                    'det_date', 'coll_p_no', 'ref', 'link2',
                    'lat_long', 'datum')

admin.site.register(DataTable)
admin.site.register(SlotData, SlotDataAdmin)
