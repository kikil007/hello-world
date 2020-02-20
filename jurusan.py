from odoo import api, fields, models #memanggil fungsi yanga ada di  odoo

class jurusan(models.Model):
    _name   = "academic.jurusan"

    name    = fields.Char("name", required=True)
    description = fields.Text("Description")
    responsible_id  = fields.Many2one (
                                        comodel_name="res.users", #res user adalah tabel base dari odoo
                                        string= "Responsible", required=True
                                        )

