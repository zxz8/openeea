# -*- coding: utf-8 -*-
{
    'name': 'Estadistica Aplicada',
    'version': '0.1',
    'category': 'Customization',
    'summary': 'Personalizacion de funciones para Estadistica Aplicada',
    'description': 'EA Custom',
    'author': 'H&D Datentechnik Mexico',
    'website': 'https://www.hud.com.mx',
    'depends': [
        'stock',
        'hr',
        'hr_contract',
        'hr_holidays', 
        'project',
        'estadistica_aplicada2',
        'account',
        'hr_payroll',
        'purchase',
        'account_asset',
        'survey',
        'sale_crm',
    ],
    'update_xml': [
        #Archivos que se actualizan cada vez que se reinicia e serivior
    ],
    'data': [
        'security/groups.xml',
        'sequence/solicitud_sequence.xml',
        'sequence/plaza_sequence.xml',
        'sequence/servicio_sequence.xml',
        'sequence/avance_sequence.xml',
        'view/avance_view.xml',
        'wizard/avance_wizard.xml',
        'view/movimientosinternos_view.xml',
        'view/tipoestudio_view.xml',
        'view/crm.xml',
        'view/saleorder_view.xml',
        'view/presupuesto_view.xml',
        'view/partner_view.xml',
        'view/crmlead_view.xml',
        'view/project_view.xml',
        'view/encuesta_view.xml',
        'view/cuota_view.xml',
        'view/gasto_view.xml',
        'view/rhbonos_view.xml',
        'view/rhdescuentos_view.xml',
        'view/rhes_view.xml',
        'view/rhasistencias_view.xml',
        'view/rhemployee_view.xml',
        'view/prenomina_view.xml',
        'view/conceptopago_view.xml',
        'view/concepto_presupuesto_view.xml',
        'view/reporte_proyecto_view.xml',
        'view/incidencia_view.xml',
        'view/lineasprenomina_view.xml',
        'view/purchaseorder_view.xml',
        'view/account_view.xml',
        'view/hrpayslip_view.xml',
        'view/asset_view.xml',
        'view/solicitud_view.xml',
        'view/picking_view.xml',
        'view/entrega_view.xml',
        'view/plaza_view.xml',
        'view/diseno_view.xml',
        'view/makesale_view.xml',
        'view/department_view.xml',
        'view/job_view.xml',
        'view/invoice_view.xml',
        'view/applicant_view.xml',
        'view/loader_view.xml',
        'view/event_view.xml',
        'view/helpdesk_view.xml',
        'view/calendario_view.xml',
        'view/auditoria_view.xml',
        'view/oficina_view.xml',
        'view/colonia_view.xml',
        'view/acuerdo_view.xml',
        'view/conciliacion_view.xml',
        'view/invoice_view.xml',
        'view/servicio_view.xml',
        'view/extra_view.xml',
        'view/user_view.xml',
        'view/externo_view.xml',
        'view/bank_view.xml', 
        'view/costo_view.xml',
        'view/hollyday_view.xml',
        'view/odt_view.xml',
        'wizard/cruces_wizard.xml',
        'workflow/encuesta_workflow.xml',
        'workflow/gasto_workflow.xml',
        'workflow/avance_workflow.xml',
        'workflow/rhbonos_workflow.xml',
        'workflow/rhdescuentos_workflow.xml',
        'workflow/rhasistencias_workflow.xml',
        'workflow/prenomina_workflow.xml',
        'workflow/controlencuesta_workflow.xml',
        'workflow/solicitud_workflow.xml',
        'workflow/diseno_workflow.xml',
        'workflow/servicio_workflow.xml',
    ],
    'demo': [
        #Aqui van datos de demostración
    ],
    'test': [
        #Archivos de testing
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [
    ],
    'css': ['static/src/css/base.css'],
    'qweb': [
        'static/src/xml/base.xml'],
    'js': ['static/src/js/chrome.js'],
}
