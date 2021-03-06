# -*- coding: utf-8 -*-
#IStandForFreedom
from osv import osv, fields


class jmdgastos(osv.Model):
    _inherit = "mail.thread"
    _name = "ea.gasto"

    def action_solicitado(self, cr, uid, ids):
            self.write(cr, uid, ids, {'state': 'solicitado'})
            return True

    def action_capturado(self, cr, uid, ids):
            self.write(cr, uid, ids, {'state': 'capturado'})
            return True

    def action_aprobado(self, cr, uid, ids):
            self.write(cr, uid, ids, {'state': 'aprobado'})
            return True

    def action_enviado(self, cr, uid, ids):
            self.write(cr, uid, ids, {'state': 'enviado'})
            return True

    def action_comprobaciones(self, cr, uid, ids):
            self.write(cr, uid, ids, {'state': 'comprobaciones'})
            return True

    def action_contabilidad(self, cr, uid, ids):
            self.write(cr, uid, ids, {'state': 'contabilidad'})
            return True

    def calculate_total(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        total = 0
        for i in self.browse(cr, uid, ids, context):
            for j in i.gasto_adepositar:
                if j.monto:
                    total += j.monto
            for k in i.gasto_nosedeposita:
                if k.monto:
                    total += k.monto
            for l in i.gasto_nominagea:
                if l.monto:
                    total += l.monto
            for m in i.gasto_otros:
                if m.monto:
                    total += m.monto
        ret[i.id] = total
        return ret

    def get_name(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = str(i.proyecto.name) + " " + str(i.plaza_id.name) +\
                " " + str(i.fecha)
        return ret

    def get_diferencia(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        total_comprobado = 0
        total_depositado = 0
        for i in self.browse(cr, uid, ids, context):
            for j in i.gasto_adepositar:
                if j.monto:
                    total_comprobado += j.monto
            for k in i.gasto_nosedeposita:
                if k.monto:
                    total_comprobado += k.monto
            for l in i.gasto_nominagea:
                if l.monto:
                    total_comprobado += l.monto
            for m in i.gasto_otros:
                if m.monto:
                    total_comprobado += m.monto
            for n in i.solicitud_ids:
                total_depositado += n.total_solicitud
        ret[i.id] = total_depositado - total_comprobado
        return ret

    _columns = {
            'name': fields.function(get_name, type="char",
                string="Proyecto Plaza Fecha", size=40, store=True),
            'fecha': fields.date("Fecha de Elaboración de Comprobación"),
            'plaza': fields.many2one("res.country.state.city", string="Plaza"),
            'plaza_id': fields.many2one("plaza", string="Plaza"),
            'proyecto': fields.many2one("project.project", string="Clave"),
            'nombre_corto': fields.related('proyecto', 'nombre_corto',
                string="Nombre Corto", type="char", store=True),
            'pid': fields.related("proyecto", "id", type="integer",
                string="Id Proyecto", readonly=True, store=True),
            'plid': fields.related("plaza_id", "id", type="integer",
                string="Id Plaza", readonly=True, store=True),
            'state': fields.selection([('solicitado', 'Preliminar'),
                ('capturado', 'A Comprobar'),
                ('enviado', 'Ok GAC'), ('comprobaciones', 'Ok Contabilidad'),
                ('contabilidad', 'Ok Final'),
                ('aprobado', 'Aprobado')],
                "Estado", readonly=True),
            'gasto_adepositar': fields.one2many("ea.gasto.line.adepositar",
                "relation_gasto", string="Gastos"),
            'gasto_nosedeposita': fields.one2many("ea.gasto.line.nosedeposita",
                "relation_gasto", string="Gastos"),
            'gasto_nominagea': fields.one2many("ea.gasto.line.nominagea",
                "relation_gasto", string="Gastos"),
            'gasto_otros': fields.one2many("ea.gasto.line.otros",
                "relation_gasto", string="Gastos"),
            'total': fields.function(calculate_total, string="Total del Gasto",
                 type="float", digits=(9, 2), store=True),
            'responsable': fields.many2one("hr.employee", "Responsable"),
            'solicitud_ids': fields.many2many("ea_solicitud", "gas2sol",
                string="Depósitos"),
            'diferencia': fields.function(get_diferencia,
                string="Diferencia", type="float"),
            'numero_poliza': fields.char("Nḿero de Póliza"),
            'total_deducible': fields.float("Total Deducible"),
            'total_no_deducible': fields.float("Total No Deducible"),
            'notas': fields.text("Notas"),
            'formato_vales': fields.binary("Formato Vales"),
            'nformato': fields.char("Nombre del Formato"),
            'vales_campo': fields.float("Monto de Vales Campo"),
            'vales_comprobaciones': fields.float("Monto de Vales Comprobaciones"),
            'total_comprobado_vales': fields.float("Monto de Vales Autorizado"),
        }


class jmdgastos(osv.Model):
    _name = "ea.gasto.line.adepositar"

    def get_proyecto(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = 0
            if i.relation_gasto and i.relation_gasto.proyecto:
                ret[i.id] = i.relation_gasto.proyecto.id
        return ret

    def set_ammounts(self, cr, uid, ids, ammount, args, context=None):
        ret = {}
        print("Here")
        for i in self.browse(cr, uid, ids, context):
            monto = i.monto_campo
            ret = {'monto_original': monto, 'monto': monto}
        return {'value': ret}

    def get_plaza(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = 0
            if i.relation_gasto and i.relation_gasto.proyecto:
                ret[i.id] = i.relation_gasto.plaza_id.id
        return ret

    _columns = {
            'name': fields.char(string="Nombre", size=40),
            'presupuesto_linea_id': fields.many2one("ea.presupuesto.concepto",
                string="Concepto"),
            'monto': fields.float(digits=(9, 2), string="Monto"),
            'rechazado': fields.boolean("Modificado"),
            'monto_original': fields.float("Monto Comprobaciones"),
            'monto_campo': fields.float("Monto Campo"),
            'numero_comprobante': fields.char(string="Numero de Comprobante",
                size=40),
            'documento': fields.binary("Comprobante"),
            'ndocumento': fields.char("Nombre Comprobante"),
            'relation_gasto': fields.many2one("ea.gasto"),
            'observaciones': fields.text("Observaciones"),
            'presupuestado_id': fields.many2one("ea.concepto_adepositar",
                string="Presupuesto"),
            'idproyecto': fields.function(get_proyecto, string="Id Proyecto",
                type="integer"),
            'idplaza': fields.function(get_plaza, string="Id Plaza",
                type="integer"),
        }


class jmdnosedeposita(osv.Model):
    _name = "ea.gasto.line.nosedeposita"

    def get_proyecto(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = 0
            if i.relation_gasto and i.relation_gasto.proyecto:
                ret[i.id] = i.relation_gasto.proyecto.id
        return ret

    def get_plaza(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = 0
            if i.relation_gasto and i.relation_gasto.proyecto:
                ret[i.id] = i.relation_gasto.plaza_id.id
        return ret

    _columns = {
            'name': fields.char(string="Nombre", size=40),
            'presupuesto_linea_id': fields.many2one("ea.presupuesto.concepto",
                string="Concepto"),
            'monto': fields.float(digits=(9, 2), string="Monto"),
            'rechazado': fields.boolean("Modificado"),
            'monto_original': fields.float("Monto Comprobaciones"),
            'monto_campo': fields.float("Monto Campo"),
            'numero_comprobante': fields.char(string="Numero de Comprobante",
                size=40),
            'documento': fields.binary("Comprobante"),
            'ndocumento': fields.char("Nombre Comprobante"),
            'relation_gasto': fields.many2one("ea.gasto"),
            'observaciones': fields.text("Observaciones"),
            'presupuestado_id': fields.many2one("ea.concepto_nosedeposita",
                string="Presupuesto"),
            'idproyecto': fields.function(get_proyecto, string="Id Proyecto",
                type="integer"),
            'idplaza': fields.function(get_plaza, string="Id Plaza",
                type="integer"),
        }


class jmdnominagea(osv.Model):
    _name = "ea.gasto.line.nominagea"

    def get_proyecto(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = 0
            if i.relation_gasto and i.relation_gasto.proyecto:
                ret[i.id] = i.relation_gasto.proyecto.id
        return ret

    def get_plaza(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = 0
            if i.relation_gasto and i.relation_gasto.proyecto:
                ret[i.id] = i.relation_gasto.plaza_id.id
        return ret

    _columns = {
            'name': fields.char(string="Nombre", size=40),
            'presupuesto_linea_id': fields.many2one("ea.presupuesto.concepto",
                string="Concepto"),
            'monto': fields.float(digits=(9, 2), string="Monto"),
            'rechazado': fields.boolean("Modificado"),
            'monto_original': fields.float("Monto Comprobaciones"),
            'monto_campo': fields.float("Monto Campo"),
            'numero_comprobante': fields.char(string="Numero de Comprobante",
                size=40),
            'documento': fields.binary("Comprobante"),
            'ndocumento': fields.char("Nombre Comprobante"),
            'relation_gasto': fields.many2one("ea.gasto"),
            'observaciones': fields.text("Observaciones"),
            'presupuestado_id': fields.many2one("ea.concepto_nominagea",
                string="Presupuesto"),
            'idproyecto': fields.function(get_proyecto, string="Id Proyecto",
                type="integer"),
            'idplaza': fields.function(get_plaza, string="Id Plaza",
                type="integer"),
        }


class jmdotros(osv.Model):
    _name = "ea.gasto.line.otros"

    def get_proyecto(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = 0
            if i.relation_gasto and i.relation_gasto.proyecto:
                ret[i.id] = i.relation_gasto.proyecto.id
        return ret

    def get_plaza(self, cr, uid, ids, fieldname, args, context=None):
        ret = {}
        for i in self.browse(cr, uid, ids, context):
            ret[i.id] = 0
            if i.relation_gasto and i.relation_gasto.proyecto:
                ret[i.id] = i.relation_gasto.plaza_id.id
        return ret

    _columns = {
            'name': fields.char(string="Nombre", size=40),
            'presupuesto_linea_id': fields.many2one("ea.presupuesto.concepto",
                string="Concepto"),
            'monto': fields.float(digits=(9, 2), string="Monto"),
            'rechazado': fields.boolean("Modificado"),
            'monto_original': fields.float("Monto Comprobaciones"),
            'monto_campo': fields.float("Monto Campo"),
            'numero_comprobante': fields.char(string="Numero de Comprobante",
                size=40),
            'documento': fields.binary("Comprobante"),
            'ndocumento': fields.char("Nombre Comprobante"),
            'relation_gasto': fields.many2one("ea.gasto"),
            'observaciones': fields.text("Observaciones"),
            'presupuestado_id': fields.many2one("ea.concepto_otros",
                string="Presupuesto"),
            'idproyecto': fields.function(get_proyecto, string="Id Proyecto",
                type="integer"),
            'idplaza': fields.function(get_plaza, string="Id Plaza",
                type="integer"),
        }
