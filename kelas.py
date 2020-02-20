# memanggil fungsi yanga ada di  odoo
from odoo import api, fields, models  

#disini kita mengguanakan many to one
class Kelas(models.Model):
    _name = "academic.kelas"

    name = fields.Char("Nama", required=True)
    jurusan_id = fields.Many2one(comodel_name="academic.jurusan",
                                 string="Jurusan")

    dosen_id = fields.Many2one(
        comodel_name="res.partner",
        string="Dosen Pengampu")

    start_date  = fields.Date       ("Start Date")
    sks         = fields.Integer    ("SKS")
    seats       = fields.Integer    ("Seats")
    active      = fields.Boolean    ("Is Active", default=True) 