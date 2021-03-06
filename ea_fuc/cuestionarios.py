# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from openerp.osv import fields, osv

class archivos(osv.Model):
    _name = 'document.archivos'
    _columns = {
        'archivo_id': fields.integer('Secuencia'),
        'nom_archivo': fields.char('Nombre de archivo'),
        'ver_archivo': fields.char('Version',size=10)
    }

class cuestionarios(osv.Model):
    _name = 'document.cuestionarios'
    _description = 'Tabla para registro de cuestionarios'
    _columns = {
        'nom_estudio_id': fields.many2one('project.arranques','Nombre del estudio'),
        'nom_responsable_id': fields.many2one('hr.employee','Responsable'),
        'responsable': fields.date('Fecha de solicitud'),
        'archivo_ids': fields.one2many('document.archivos','archivo_id','Archivos')
    }
