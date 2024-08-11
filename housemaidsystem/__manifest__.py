# -*- coding: utf-8 -*-
{
    'name': "Housemaid System",

    'summary': """
        Sample application for housemaidsystem offices daily operations
    """,

    'author': "Bassam Mannaa",
    'website': "https://housemaidsystem.bassammannaa.com/",
    'category': 'Business',
    'version': '14.1.3',
    'license': 'AGPL-3',
    'depends': ['base', 'account', 'crm', 'l10n_sa', 'mail'],
    'images': [
        'static/description/icon.jpeg', ],
    'data': [
        # Security
        'security/housemaid_security.xml',
        'security/ir.model.access.csv',

        # viwes
        'views/externaloffices.xml',
        'views/postapplied.xml',
        'views/religion.xml',
        'views/sponsor_occupation.xml',
        'views/sponsor_house_type.xml',
        'views/education.xml',
        'views/externalofficetransdet.xml',
        'views/cancel_application.xml',
        'views/activate_application.xml',
        'views/applications.xml',
        'views/reservations.xml',
        'views/visa.xml',
        'views/expectedarrival.xml',
        'views/arrival.xml',
        'views/deliver.xml',
        'views/return_back_from_first_sponsor.xml',
        'views/return_back_from_last_sponsor.xml',
        'views/account_invoice.xml',
        'views/returnback.xml',
        'views/externalofficetransdet.xml',
        'views/resell.xml',
        'views/selltest.xml',
        'views/office_branches.xml',
        'views/account_items.xml',
        'views/system_support.xml',
        'views/res_config_settings.xml',
        'views/reports_setup.xml',
        'views/dashboard.xml',
        'views/sponsor_payments.xml',
        'views/back_to_country_after_first_sponsor.xml',
        'views/back_to_country_after_last_sponsor.xml',
        'views/collect_payment_late.xml',
        'views/contracts_print.xml',
        'views/customers.xml',


        # data
        'data/post_applied_data.xml',
        'data/education_data.xml',
        'data/religion_data.xml',
        'data/externalofficetransdet.xml',
        'data/system_reports_data.xml',
        'data/occupation_data.xml',
        'data/house_type_data.xml',
        'data/state_data.xml',

        # reports (new)
        'report/application_activation_rep.xml',
        'report/application_cancellation_rep.xml',
        'report/reservations_list_rep.xml',
        'report/application_list_rep.xml',
        'report/visa_list_rep.xml',
        'report/expected_arrival_list_rep.xml',
        'report/arrival_list_rep.xml',
        'report/deliver_list_rep.xml',
        'report/contract_print.xml',
        'report/civilid_print.xml',
        'report/visa_translate_print.xml',

        # reports (old)
        'report/list_reservations.xml',
        'report/application_details_report.xml',
        'report/list_canceled_applications.xml',
        'report/list_activated_applications.xml',
        'report/list_visa.xml',
        'report/list_expectedarrival.xml',
        'report/list_arrival.xml',
        'report/list_deliver.xml',
        # wizard
        'wizard/application_activation_wz.xml',
        'wizard/application_cancellation_wz.xml',
        'wizard/reservations_list_wz.xml',
        'wizard/application_list_wz.xml',
        'wizard/visa_list_wz.xml',
        'wizard/arrival_list_wz.xml',
        'wizard/expected_arrival_list_wz.xml',
        'wizard/deliver_list_wz.xml',
        # menus
        'views/menus.xml',
        # 'views/website_application_list.xml'
    ],
    'demo': [
        # 'demo/externaloffices.xml',
        # 'demo/applications.xml',
        # 'demo/reservations.xml',
        # 'demo/visa.xml',
        # 'demo/expectedarrival.xml',
        # 'demo/arrival.xml',
        # 'demo/deliver.xml',
    ],
    'price': 300,
    'currency': 'USD',
    'application': True,
    'installable': True,
    'auto_install': False,
    'post_init_hook': '_setup_main_configuration',
}
