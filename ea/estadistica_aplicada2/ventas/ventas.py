# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class cuentas(osv.Model):
    _inherit = 'res.partner'
    _description = 'Campos personalizados nuevo cliente'
    _columns = {
        'tipo_cuenta': fields.selection([('chica', 'Chica'),
            ('mediana', 'Mediana'), ('grande', 'Grande')], "Tipo de cuenta"),
        'es_gea': fields.boolean("Grupo Estadística Aplicada"),
    }


class informes(osv.Model):
    _inherit = 'sale.order'
    _description = 'Campos personalizados analisis desempeno de ventas'
    _columns = {
        'tipo_estudio': fields.selection((('conjoint', 'Conjoint'),
            ('ua', 'U&A'), ('tracking', 'Tracking')), "Tipo de estudio"),
    }


class ordenes(osv.Model):
    _inherit = 'mrp.production.workcenter.line'
    _description = 'Campos personalizados ordenes de trabajo'
    _columns = {
        'responsable': fields.char(string='Responsable', required=True)
    }