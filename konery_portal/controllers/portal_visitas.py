# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.exceptions import AccessError, MissingError
from odoo.http import request


class PortalVT(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super(PortalVT, self)._prepare_portal_layout_values()
        vt_count = request.env['x_cuestionarios'].search_count([])
        values['vt_count'] = vt_count
        return values

    def _vt_get_page_view_values(self, vt, access_token, **kwargs):
        values = {
            'page_name': 'vt',
            'vt': vt,
        }
        return self._get_page_view_values(vt, access_token, values, 'my_vts_history', False, **kwargs)

    @http.route(['/my/vt', '/my/vt/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_vts(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        VT = request.env['x_cuestionarios']

        domain = []

        searchbar_sortings = {
            'date': {'label': _('Report Date'), 'order': 'x_informe_date desc'},
            'name': {'label': _('Reference'), 'order': 'x_name desc'},
            'type': {'label': _('Type'), 'order': 'x_tipo_id'},
        }
        # default sort by order
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        archive_groups = self._get_archive_groups('account.invoice', domain)
        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        # count for pager
        vt_count = VT.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/vts",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=vt_count,
            page=page,
            step=self._items_per_page
        )
        # content according to pager and archive selected
        vts = VT.search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_vts_history'] = vts.ids[:100]

        values.update({
            'date': date_begin,
            'vts': vts,
            'page_name': 'vt',
            'pager': pager,
            'archive_groups': archive_groups,
            'default_url': '/my/vts',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("konery_portal.portal_my_vts", values)

    @http.route(['/my/vts/<int:vt_id>'], type='http', auth="public", website=True)
    def portal_my_vt_detail(self, vt_id, access_token=None, report_type=None, download=False, **kw):
        try:
            vt_sudo = self._document_check_access('x_cuestionarios', vt_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(
                model=vt_sudo,
                report_type=report_type,
                report_ref='studio_customization.cuestionarios_report_b1b85f62-563d-4e45-8d9e-e7776704396b',
                download=download)

        values = self._vt_get_page_view_values(vt_sudo, access_token, **kw)
        PaymentProcessing.remove_payment_transaction(vt_sudo.transaction_ids)
        return request.render("konery_portal.portal_vt_page", values)