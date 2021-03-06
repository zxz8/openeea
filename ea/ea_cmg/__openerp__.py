# -*- coding: utf-8 -*-
{
    'name': 'Cambio de etiqueta para menú Proyecto',
    'version': '0.1',
    'category': 'Customization',
    'summary': 'Personalización de funciones para Estadistica Aplicada',
    'description': '''
        Funciones personalizados por: H&D Datentechnik Mexico, para la empresa: Estadistica Aplicada
        Cambios en aplicaciones:
            - Modificacion en la pestaña de 'Estudios' para el menú de Proyecto pasa a Orden de trabajo
            - Cambio de etiquetas en Proyectos, Arranques y Campo
        Responsable del modulo: Carlos E. Mendoza González
    ''',
    'depends': [
        'base',
        'crm','crm_todo',
        'mrp','mrp_operations','mrp_repair',
        'project',
        'project_mrp','project_issue','pad_project',
        'purchase',
        'hr',
        'hr_evaluation',
        'stock',
        'sale_stock',
        'knowledge',
        'event',
        'document',
        'l10n_mx_cities',
        'l10n_mx_sale_payment_method','l10n_mx_purchase_payment_method',
        'l10n_mx_account_invoice_tax','l10n_mx_facturae_pac_sf',
        'account',
        'project',
        'analytic',
        'survey',
        'project_issue',
        'estadistica_aplicada2'
    ],
    'author': 'H&D Datentechnik Mexico',
    'category': 'Customization',
    'description': 'Modificación al menu bar',
    'update_xml': [],
    'data': [
        'Security/workflow_security.xml',
        'Security/ir.model.access.csv',
        'View/cambios_etiquetas_estudios_proyectos.xml',
        'View/cambio_etiquetas_tree_etapas_pc.xml',
        'View/menu_presentacion_cmg.xml',
        'Workflow/workflow_presentacion_cmg.xml',
        'View/presentacion_view_cmg.xml',
        'View/menu_validacion_cmg.xml',
        'View/validacion_view_cmg.xml'
    ],
    'demo': [
        #Aqui van datos de demostración
    ],
    'test': [#Archivos de testing
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    }



