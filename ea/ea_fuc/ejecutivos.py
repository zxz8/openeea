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

class ejecutivos(osv.Model):
    _name = 'ejecutivos.cuenta'
    _description = 'Modulo de Ejecutivos de Cuenta, menu Ejecutivos de Cuenta'
    _columns = {
        'name': fields.text("Nombre")
    }

class llamadas(osv.Model):
    _inherit = 'crm.phonecall'
    _description = 'Alteracion de campos personalizados'
    _columns = {
        'categoria': fields.selection([('entrantes','Llamada entrante'),('salientes','Llamada saliente')],'Categoria')
    }
